from abc import ABC, abstractmethod

class PurchaseSubscriptionRepository(ABC):

    @abstractmethod
    def create(self, purchase, purchase_subscription):
        pass

    @abstractmethod
    def findByPurchaseId(self, purchaseId):
        pass