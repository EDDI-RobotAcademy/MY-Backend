from account.entity.account import Account
from like_count.entity.like_count import LikeCount
from like_count.repository.like_count_repository import LikeCountRepository
from smart_content.entity.models import SmartContent


class LikeCountRepositoryImpl(LikeCountRepository):
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

    def toggleLike(self, accountId, contentId):
        account = Account.objects.get(id=accountId)
        smart_content = SmartContent.objects.get(id=contentId)
        like, created = LikeCount.objects.get_or_create(
            account=account,
            smart_content=smart_content
        )
        if not created:
            like.delete()
            return False
        return True

    def getLikeCount(self, contentId):
        return LikeCount.objects.filter(smart_content_id=contentId).count()

