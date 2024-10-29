from abc import ABC, abstractmethod

class SmartContentService(ABC):
    @abstractmethod
    def create(self, title, content_type, items, nickname, accountId):
        pass

    @abstractmethod
    def list(self, page_number=1, items_per_page=6):
        pass

    @abstractmethod
    def listByAccountId(self, accountId, page_number=1, items_per_page=6):
        pass

    @abstractmethod
    def listItems(self, contentId):
        pass

    @abstractmethod
    def read(self, contentId):
        pass