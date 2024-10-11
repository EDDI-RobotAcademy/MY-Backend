from abc import ABC, abstractmethod

class SubscriptionRepository(ABC):

    @abstractmethod
    def create(self, name, type, price):
        pass