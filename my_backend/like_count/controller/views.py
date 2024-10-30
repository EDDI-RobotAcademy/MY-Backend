from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from like_count.service.like_count_service_impl import LikeCountServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
from smart_content.service.smart_content_service_impl import SmartContentServiceImpl


class LikeCountView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    smartContentService = SmartContentServiceImpl.getInstance()
    likeCountService = LikeCountServiceImpl.getInstance()

    def toggleLike(self, request):
        try:
            userToken = request.data.get('userToken')
            contentId = request.data.get('content_id')

            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None

            liked = self.likeCountService.toggleLike(accountId, contentId)

            return Response({'liked': liked}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def getLikeCount(self, request):
        try:
            contentId = request.data.get('content_id')
            likeCount = self.likeCountService.getLikeCount(contentId)

            return Response({'likeCount': likeCount}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

