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
        commentsList = self.freeCommunityCommentService.listComments(freeCommmunityId)
        serializer = FreeCommunityCommentSerializer(commentsList, many=True)
        return Response(serializer.data)

    def listReplies(self, request):
        parentId = request.data.get('parent_id')
        repliesList = self.freeCommunityCommentService.listReplies(parentId)
        serializer = FreeCommunityCommentSerializer(repliesList, many=True)
        return Response(serializer.data)

    def createComment(self, request):
        try:
            data = request.data
            freeCommmunityId = data.get('free_community_id')
            parentId = data.get('parent_id', None)
            content = data.get('content')
            userToken = data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None

            print(
                f"freeCommmunityId: {freeCommmunityId}, parentId: {parentId}, accountId: {accountId}, content: {content}")

            self.freeCommunityCommentService.createComment(content, freeCommmunityId, accountId, parentId)
            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)


