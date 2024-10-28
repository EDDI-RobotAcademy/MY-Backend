from abc import ABC,abstractmethod

class SmartContentRepository(ABC):
    @abstractmethod
    def create(self, title, content_type, items, nickname, accountId):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def listItems(self, contentId):
        pass

    @abstractmethod
    def findByContentId(self, contentId):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass