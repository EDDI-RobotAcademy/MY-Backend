from abc import ABC, abstractmethod

class SmartContentService(ABC):
    @abstractmethod
    def create(self, title, content_type, items, accountId):
        pass

    @abstractmethod
    def list(self):
        pass