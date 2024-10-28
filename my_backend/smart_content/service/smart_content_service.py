from abc import ABC, abstractmethod

class SmartContentService(ABC):
    @abstractmethod
    def create(self, title, content_type, items, nickname, accountId):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def listByAccountId(self, accountId):
        pass

    @abstractmethod
    def listItems(self, contentId):
        pass

    @abstractmethod
    def read(self, contentId):
        pass