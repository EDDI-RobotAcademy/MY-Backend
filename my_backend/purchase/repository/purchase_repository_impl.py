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