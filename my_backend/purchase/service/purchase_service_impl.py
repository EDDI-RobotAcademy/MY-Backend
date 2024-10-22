from purchase.repository.purchase_repository_impl import PurchaseRepositoryImpl
from purchase.repository.purchase_subscription_repository_impl import PurchaseSubscriptionRepositoryImpl
from purchase.service.purchase_service import PurchaseService


class PurchaseServiceImpl(PurchaseService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__purchaseRepository = PurchaseRepositoryImpl.getInstance()
            cls.__instance.__purchaseSubscriptionRepository = PurchaseSubscriptionRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createPurchase(self, accountId, purchase_subscription):
        try:
            purchase = self.__purchaseRepository.create(accountId)
            print("purchase : ", purchase, "purchase_subscription : ", purchase_subscription)
            self.__purchaseSubscriptionRepository.create(purchase, purchase_subscription)

            return purchase.id

        except Exception as e:
            print('Error creating purchase:', e)
            raise e
