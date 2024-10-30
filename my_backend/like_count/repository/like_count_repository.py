from abc import ABC, abstractmethod

class LikeCountRepository(ABC):
    @abstractmethod
    def toggleLike(self, accountId, contentId):
        pass

    @abstractmethod
    def getLikeCount(self, contentId):
        pass