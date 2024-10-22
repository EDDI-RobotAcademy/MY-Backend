from purchase.repository.purchase_repository_impl import PurchaseRepositoryImpl
from purchase.repository.purchase_subscription_repository_impl import PurchaseSubscriptionRepositoryImpl
from purchase.service.purchase_service import PurchaseService
from datetime import timedelta
from django.utils import timezone

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

    def getRecentPurchaseSubscription(self, accountId):
        try:
            recentpurchase = self.__purchaseRepository.findRecentPurchaseByAccountId(accountId)

            if isinstance(recentpurchase, Exception):
                return {'message': 'No purchase history', 'recent_subscription': None}

            current_time = timezone.now()

            if recentpurchase.created_date >= current_time - timedelta(days=30):
                recentpurchasedsubscription = self.__purchaseSubscriptionRepository.findByPurchaseId(recentpurchase)
                return recentpurchasedsubscription
            else:
                return {'message': 'More than one month since last purchase', 'recent_subscription': None}
        except Exception as e:
            print('구독 기록 확인 중 문제 발생: ', e)
            return {'error' : str(e)}



