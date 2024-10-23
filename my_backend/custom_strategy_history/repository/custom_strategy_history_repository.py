from abc import ABC, abstractmethod


class CustomStrategyHistoryRepository(ABC):
    @abstractmethod
    def addToStrategyHistory(self, accountId, aiResult):
        pass