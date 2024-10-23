from abc import ABC, abstractmethod

class PurchaseRepository(ABC):
    @abstractmethod
    def create(self, accountId):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass

    @abstractmethod
    def findRecentPurchaseByAccountId(self, accountId):
        pass
