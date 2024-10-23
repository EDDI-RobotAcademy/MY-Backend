from abc import ABC, abstractmethod
class FreeCommunityRepository(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create_category(self, name):
        pass

    @abstractmethod
    def create(self, categoryId, title, accountId, content, contentImage):
        pass

    @abstractmethod
    def findByFreeCommunityId(self, free_communityId):
        pass

    @abstractmethod
    def deleteByFreeCommunityId(self, free_communityId):
        pass

    @abstractmethod
    def update(self, free_community, free_communityData):
        pass

    @abstractmethod
    def get_all_categories(self):
        pass

    @abstractmethod
    def listFreeCommunityByCategoryId(self, categoryId):
        pass

    @abstractmethod
    def listFreeCommunityByTitle(self, title):
        pass

    @abstractmethod
    def listFreeCommunityByContent(self, content):
        pass

    @abstractmethod
    def listFreeCommunityByAccount(self, accounts):
        pass