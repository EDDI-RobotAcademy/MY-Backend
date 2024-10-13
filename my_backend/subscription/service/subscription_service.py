from abc import ABC, abstractmethod


class SubscriptionService(ABC):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, name, type, price):
        pass

    @abstractmethod
    def read(self, subscriptionId):
        pass