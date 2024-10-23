from abc import ABC, abstractmethod
class FreeCommunityService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createCategory(self, name):
        pass

    @abstractmethod
    def createFreeCommunity(self, categoryId, title, accountId, content, contentImage):
        pass

    @abstractmethod
    def readFreeCommunity(self, free_communityId):
        pass

    @abstractmethod
    def removeFreeCommunity(self, free_communityId):
        pass

    @abstractmethod
    def updateFreeCommunity(self, free_communityId, free_communityData):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass

    @abstractmethod
    def listByCategoryId(self, categoryId):
        pass

    @abstractmethod
    def listByTitle(self, title):
        pass

    @abstractmethod
    def listByContent(self, content):
        pass

    @abstractmethod
    def listByNickname(self, nickname):
        pass