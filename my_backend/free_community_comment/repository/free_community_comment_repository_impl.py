from account.entity.account import Account
from free_community.entity.models import FreeCommunity
from free_community_comment.entity.models import FreeCommunityComment
from free_community_comment.repository.free_community_comment_repository import FreeCommunityCommentRepository


class FreeCommunityCommentRepositoryImpl(FreeCommunityCommentRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, free_community_id):
        return FreeCommunityComment.objects.filter(free_community=free_community_id).order_by('regDate')

    def list_replies(self, parent_id):
        return FreeCommunityComment.objects.filter(parent=parent_id).order_by('regDate')

    def create(self, content, free_community_id, account_id, parent_id=None):
        free_community = FreeCommunity.objects.get(free_communityId=free_community_id)
        if account_id:
            account = Account.objects.get(id=account_id)
        else:
            account = None

        parent_comment = FreeCommunityComment.objects.get(commentId=parent_id) if parent_id else None

        free_community_comment = FreeCommunityComment(
            content=content,
            free_community=free_community,
            account=account,
            parent=parent_comment
        )
        free_community_comment.save()
        return free_community_comment

    def findByCommentId(self, comment_id):
        return FreeCommunityComment.objects.get(commentId=comment_id)

    def deleteByCommentId(self, comment_id):
        comment = FreeCommunityComment.objects.get(commentId=comment_id)
        comment.delete()

    def update(self, comment, commentData):
        for key, value in commentData.items():
            print(f"key: {key}, value: {value}")
            setattr(comment, key, value)
        comment.save()
        return comment