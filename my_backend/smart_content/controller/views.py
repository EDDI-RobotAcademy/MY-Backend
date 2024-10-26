from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from redis_token.service.redis_service_impl import RedisServiceImpl
from smart_content.entity.models import SmartContent
from smart_content.serializers import SmartContentSerializer
from smart_content.service.smart_content_service_impl import SmartContentServiceImpl


class SmartContentView(viewsets.ViewSet):
    queryset = SmartContent.objects.all()

    smartContentService = SmartContentServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def create(self, request):
        try:
            data = request.data
            title = data.get('title')
            content_type = data.get('content_type')
            items = data.get('items', [])
            userToken = data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None

            smart_content = self.smartContentService.create(title, content_type, items, accountId)
            return Response({'smart content 등록 성공'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('smart content 등록 과정 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        smartContentList = self.smartContentService.list()
        serializer = SmartContentSerializer(smartContentList, many=True)

        return Response(serializer.data)





