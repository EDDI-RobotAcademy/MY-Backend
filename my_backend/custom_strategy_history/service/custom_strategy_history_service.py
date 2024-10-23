from abc import ABC, abstractmethod


class CustomStrategyHistoryService(ABC):
    @abstractmethod
    def saveStrategyData(self, accountId, aiResult):
        pass