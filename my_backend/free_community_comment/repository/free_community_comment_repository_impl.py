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