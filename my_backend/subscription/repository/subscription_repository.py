from abc import ABC, abstractmethod

class SubscriptionRepository(ABC):

    @abstractmethod
    def create(self, name, type, description, price):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def findById(self, subscriptionId):
        pass

    @abstractmethod
    def deleteById(self, subscriptionId):
        pass

    @abstractmethod
    def update(self, subscriptionId, subscriptionData):
        pass