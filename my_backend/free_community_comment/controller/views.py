from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from free_community_comment.entity.models import FreeCommunityComment
from free_community_comment.serializers import FreeCommunityCommentSerializer
from free_community_comment.service.free_community_comment_service_impl import FreeCommunityCommentServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl


class FreeCommunityCommentView(viewsets.ViewSet):
    queryset = FreeCommunityComment.objects.all()

    freeCommunityCommentService = FreeCommunityCommentServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def listComments(self, request):
        freeCommmunityId = request.data.get('free_community_id')
        commentsList = self.freeCommunityCommentService.listComment(freeCommmunityId)
        serializer = FreeCommunityCommentSerializer(commentsList, many=True)
        return Response(serializer.data)