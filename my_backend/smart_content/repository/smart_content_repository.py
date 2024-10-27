from abc import ABC,abstractmethod

class SmartContentRepository(ABC):
    @abstractmethod
    def create(self, title, content_type, items, accountId):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def listItems(self, contendId):
        pass