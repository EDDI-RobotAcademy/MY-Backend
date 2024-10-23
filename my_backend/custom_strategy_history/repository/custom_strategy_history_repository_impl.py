from account.entity.account import Account
from custom_strategy_history.entity.custom_strategy_history import CustomStrategyHistory
from custom_strategy_history.repository.custom_strategy_history_repository import CustomStrategyHistoryRepository


class CustomStrategyHistoryRepositoryImpl(CustomStrategyHistoryRepository):
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

    def addToStrategyHistory(self, accountId, aiResult):
        try:
            account = Account.objects.get(id=int(accountId))
            customStrategyHistory = CustomStrategyHistory(
                account=account,
                strategy_result=aiResult
            )
            customStrategyHistory.save()

        except Account.DoesNotExist:
            print("해당 Account가 존재하지 않습니다.")

        return customStrategyHistory
