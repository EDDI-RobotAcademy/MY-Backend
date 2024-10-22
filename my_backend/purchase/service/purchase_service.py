from abc import ABC, abstractmethod

class PurchaseService(ABC):
    @abstractmethod
    def createPurchase(self, accountId, purchase_subscription):
        pass

    @abstractmethod
    def getRecentPurchaseSubscription(self, accountId):
        pass