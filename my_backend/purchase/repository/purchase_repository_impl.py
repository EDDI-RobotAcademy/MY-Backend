from account.entity.account import Account
from purchase.entity.purchase import Purchase
from purchase.repository.purchase_repository import PurchaseRepository


class PurchaseRepositoryImpl(PurchaseRepository):
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

    def create(self, accountId):
        account = Account.objects.get(id = accountId)
        purchase = Purchase(account=account)
        purchase.save()

        return purchase

    def findByAccountId(self, accountId):
        account = Account.objects.get(id = accountId)
        try:
            purchase = Purchase.objects.get(account=account)
            return purchase
        except Exception as e:
            print('구독권을 구매한 기록이 없습니다.', e)
            return None

    def findRecentPurchaseByAccountId(self, accountId):
        try:
            account = Account.objects.get(id=accountId)
            recentPurchase = Purchase.objects.filter(account=account).order_by('-created_date').first()

            if recentPurchase:
                return recentPurchase
            else:
                print("구매 기록이 없습니다.")
                return None
        except Account.DoesNotExist:
            print(f"Account with id {accountId} does not exist.")
            return None
        except Exception as e:
            print('구매 기록을 가져오는 중 묹제 발생: ', e)
            return None



