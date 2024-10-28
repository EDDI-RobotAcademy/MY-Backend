from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from redis_token.service.redis_service_impl import RedisServiceImpl
from smart_content.entity.models import SmartContent
from smart_content.serializers import SmartContentSerializer
from smart_content.service.smart_content_service_impl import SmartContentServiceImpl
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class SmartContentView(viewsets.ViewSet):
    queryset = SmartContent.objects.all()

    smartContentService = SmartContentServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    userProfileService = UserProfileServiceImpl.getInstance()

    def create(self, request):
        try:
            data = request.data
            title = data.get('title')
            content_type = data.get('content_type')
            items = data.get('items', [])
            userToken = data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
                nickname = self.userProfileService.getNicknameByAccountId(accountId)

            else:
                accountId = None

            smart_content = self.smartContentService.create(title, content_type, items, nickname, accountId)
            return Response({'smart content 등록 성공'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('smart content 등록 과정 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        smartContentList = self.smartContentService.list()
        serializer = SmartContentSerializer(smartContentList, many=True)

        return Response(serializer.data)

    def listByAccountId(self, request):
        try:
            userToken = request.data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)

            else:
                accountId = None

            smartContentList = self.smartContentService.listByAccountId(accountId)
            serializer = SmartContentSerializer(smartContentList, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print('accountId로 smart content list 출력 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def listItems(self, request):
        try:
            contentId = request.data.get('content_id')
            items = self.smartContentService.listItems(contentId)
            print(contentId, items)
            return Response({'items': items})
        except Exception as e:
            print('items list 조회 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def read(self, request, pk=None):
        smartContent = self.smartContentService.read(pk)
        if smartContent is not None:
            serializer = SmartContentSerializer(smartContent)
            return Response(serializer.data)
        else:
            return Response({"error": "Comment not found."}, status=status.HTTP_204_NO_CONTENT)






