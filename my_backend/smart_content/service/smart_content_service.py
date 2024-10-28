from abc import ABC, abstractmethod

class SmartContentService(ABC):
    @abstractmethod
    def create(self, title, content_type, items, nickname, accountId):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def listItems(self, contentId):
        pass