from abc import ABC, abstractmethod

class SubscriptionRepository(ABC):

    @abstractmethod
    def create(self, name, type, price):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def findById(self, subscriptionId):
        pass