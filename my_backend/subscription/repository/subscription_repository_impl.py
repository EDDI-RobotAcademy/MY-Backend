from subscription.entity.subscription import Subscription
from subscription.repository.subscription_repository import SubscriptionRepository


class SubscriptionRepositoryImpl(SubscriptionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Subscription.objects.all()

    def create(self, name, type, description, price):
        subscription = Subscription(
            name = name,
            type = type,
            description = description,
            price = price
        )
        subscription.save()
        return subscription

    def findById(self, subscriptionId):
        try:
            return Subscription.objects.get(id = subscriptionId)
        except Subscription.DoesNotExist:
            return None

    def deleteById(self, subscriptionId):
        subscription = Subscription.objects.get(id=subscriptionId)
        subscription.delete()

