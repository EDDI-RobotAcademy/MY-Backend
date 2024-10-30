from abc import ABC,abstractmethod

class LikeCountService(ABC):
    @abstractmethod
    def toggleLike(self, accountId, contentId):
        pass

    @abstractmethod
    def getLikeCount(self, contentId):
        pass