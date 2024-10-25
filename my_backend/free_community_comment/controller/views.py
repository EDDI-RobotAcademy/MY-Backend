from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from free_community_comment.entity.models import FreeCommunityComment
from free_community_comment.serializers import FreeCommunityCommentSerializer
from free_community_comment.service.free_community_comment_service_impl import FreeCommunityCommentServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class FreeCommunityCommentView(viewsets.ViewSet):
    queryset = FreeCommunityComment.objects.all()

    freeCommunityCommentService = FreeCommunityCommentServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    userProfileService = UserProfileServiceImpl.getInstance()

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
                nickname = self.userProfileService.getNicknameByAccountId(accountId)
            else:
                accountId = None
                nickname = "익명"

            print(
                f"freeCommmunityId: {freeCommmunityId}, parentId: {parentId}, accountId: {accountId}, "
                f"nickname: {nickname}, content: {content}")

            self.freeCommunityCommentService.createComment(content, nickname, freeCommmunityId, accountId, parentId)
            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def readComment(self, request, pk=None):
        comment = self.freeCommunityCommentService.readComment(pk)
        if comment is not None:
            serializer = FreeCommunityCommentSerializer(comment)
            return Response(serializer.data)
        else:
            return Response({"error": "Comment not found."}, status=status.HTTP_204_NO_CONTENT)

    def removeComment(self, request, pk=None):
        self.freeCommunityCommentService.removeComment(pk)
        return Response("댓글 삭제 성공", status=status.HTTP_204_NO_CONTENT)

    def modifyComment(self, request, pk=None):
        comment = self.freeCommunityCommentService.readComment(pk)
        serializer = FreeCommunityCommentSerializer(comment, data=request.data, partial=True)

        if serializer.is_valid():
            updatedComment = self.freeCommunityCommentService.updateComment(pk, serializer.validated_data)
            return Response(FreeCommunityCommentSerializer(updatedComment).data)

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

        comment = self.freeCommunityCommentService.readComment(pk)

        is_authorized = comment.account.id == accountId
        print("comment account 2", comment.account.id)
        print("accountId 2", accountId)

        return Response({'is_authorized': is_authorized}, status=status.HTTP_200_OK)

