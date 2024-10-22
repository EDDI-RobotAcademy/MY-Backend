from abc import ABC, abstractmethod

class PurchaseRepository(ABC):
    @abstractmethod
    def create(self, accountId):
        pass
