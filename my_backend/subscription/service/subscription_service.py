from abc import ABC, abstractmethod


class SubscriptionService(ABC):

    @abstractmethod
    def create(self, name, type, price):
        pass