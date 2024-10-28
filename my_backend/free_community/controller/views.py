from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import IntegrityError
from free_community.entity.models import FreeCommunity
from free_community.serializers import FreeCommunitySerializer, FreeCommunityCategorySerializer
from free_community.service.free_community_service import FreeCommunityService
from free_community.service.free_community_service_impl import FreeCommunityServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl


class FreeCommunityView(viewsets.ViewSet):
    queryset = FreeCommunity.objects.all()

    free_communityService = FreeCommunityServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def list(self, request):
        free_communityList = self.free_communityService.list()
        serializer = FreeCommunitySerializer(free_communityList, many=True)
        return Response(serializer.data)

    def listByCategory(self, request):
        categoryId = request.data.get('categoryId')
        free_communityList = self.free_communityService.listByCategoryId(categoryId)
        serializer = FreeCommunitySerializer(free_communityList, many=True)
        return Response(serializer.data)

    def listByTitle(self, request):
        print (request)
        title = request.data.get('query')
        if not title:
            return Response({"error": "Query parameter 'query' is missing."}, status=status.HTTP_400_BAD_REQUEST)
        free_communityList = self.free_communityService.listByTitle(title)
        serializer = FreeCommunitySerializer(free_communityList, many=True)
        return Response(serializer.data)

    def listByContent(self, request):
        content = request.data.get('query')
        if not content:
            return Response({"error": "Query parameter 'query' is missing."}, status=status.HTTP_400_BAD_REQUEST)
        free_communityList = self.free_communityService.listByContent(content)
        serializer = FreeCommunitySerializer(free_communityList, many=True)
        return Response(serializer.data)

    def listByNickname(self, request):
        nickname = request.data.get('query')
        if not nickname:
            return Response({"error": "Query parameter 'query' is missing."}, status=status.HTTP_400_BAD_REQUEST)
        free_communityList = self.free_communityService.listByNickname(nickname)
        serializer = FreeCommunitySerializer(free_communityList, many=True)
        return Response(serializer.data)

    def create(self, request):
        try:
            data = request.data

            categoryId = data.get('category_id')
            title = data.get('title')
            userToken = data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None
            content = data.get('content')
            contentImage = data.get('contentImage')

            print(
                f"categoryId: {categoryId}, title: {title}, accountId: {accountId}, content: {content}, contentImage: {contentImage}")

            self.free_communityService.createFreeCommunity(categoryId, title, accountId, content, contentImage)
            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def createCategory(self, request):
        serializer = FreeCommunityCategorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                category = self.free_communityService.createCategory(serializer.validated_data)
                return Response({"message": "카테고리 생성 완료"}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({"message": "이미 존재하는 카테고리입니다."}, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                return Response({"message": "카테고리 추가 중 오류가 발생했습니다."}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def getCategories(self, request):
        service = FreeCommunityServiceImpl()
        categories = service.get_all_categories()
        return Response(categories)

    def readFreeCommunity(self, request, pk=None):
        free_community = self.free_communityService.readFreeCommunity(pk)
        serializer = FreeCommunitySerializer(free_community)
        return Response(serializer.data)

    def removeFreeCommunity(self, request, pk=None):
        self.free_communityService.removeFreeCommunity(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def modifyFreeCommunity(self, request, pk=None):
        free_community = self.free_communityService.readFreeCommunity(pk)
        serializer = FreeCommunitySerializer(free_community, data=request.data, partial=True)

        if serializer.is_valid():
            updatedFreeCommunity = self.free_communityService.updateFreeCommunity(pk, serializer.validated_data)
            return Response(FreeCommunitySerializer(updatedFreeCommunity).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def checkAuthority(self, request, pk=None):
        userToken = request.data.get('userToken')
        if userToken:
            accountId = self.redisService.getValueByKey(userToken)
            try:
                accountId = int(accountId)
            except ValueError:
                accountId = None
        else:
            accountId = None

        free_community = self.free_communityService.readFreeCommunity(pk)

        is_authorized = free_community.account.id == accountId
        print("free_community account 2", free_community.account.id)
        print("accountId 2", accountId)

        return Response({'is_authorized': is_authorized}, status=status.HTTP_200_OK)

