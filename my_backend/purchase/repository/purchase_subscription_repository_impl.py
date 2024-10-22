from purchase.entity.purchase_subscription import PurchaseSubscription
from purchase.repository.purchase_subscription_repository import PurchaseSubscriptionRepository
from subscription.entity.subscription import Subscription


class PurchaseSubscriptionRepositoryImpl(PurchaseSubscriptionRepository):
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

    def create(self, purchase, purchase_subscription):
        subscription = Subscription.objects.get(id = purchase_subscription)
        purchase_subscription = PurchaseSubscription(purchase=purchase, subscription=subscription)
        purchase_subscription.save()

    def findByPurchaseId(self, purchaseId):
        purchase_subscription = PurchaseSubscription.objects.get(purchase = purchaseId)
        return purchase_subscription
