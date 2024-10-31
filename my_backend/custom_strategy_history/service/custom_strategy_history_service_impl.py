from custom_strategy_history.repository.custom_strategy_history_repository_impl import CustomStrategyHistoryRepositoryImpl
from custom_strategy_history.service.custom_strategy_history_service import CustomStrategyHistoryService


class CustomStrategyHistoryServiceImpl(CustomStrategyHistoryService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__customStrategyHistoryRepository = CustomStrategyHistoryRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def saveStrategyData(self, request_id, aiResult):
        added_strategy = self.__customStrategyHistoryRepository.addToStrategyHistory(request_id, aiResult)
        print(f"전략 저장 완료 => strategy id: {added_strategy.id}")

        return added_strategy

