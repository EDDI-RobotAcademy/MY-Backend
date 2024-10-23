from abc import ABC, abstractmethod


class SubscriptionService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, name, type, description, price):
        pass

    @abstractmethod
    def read(self, subscriptionId):
        pass

    @abstractmethod
    def removeSubscription(self, subscriptionId):
        pass