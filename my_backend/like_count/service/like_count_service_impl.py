from like_count.repository.like_count_repository_impl import LikeCountRepositoryImpl
from like_count.service.like_count_service import LikeCountService


class LikeCountServiceImpl(LikeCountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__likeCountRepository = LikeCountRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def toggleLike(self, accountId, contentId):
        return self.__likeCountRepository.toggleLike(accountId, contentId)

    def getLikeCount(self, contentId):
        return self.__likeCountRepository.getLikeCount(contentId)