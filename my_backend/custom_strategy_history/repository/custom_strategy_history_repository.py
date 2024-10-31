from abc import ABC, abstractmethod


class CustomStrategyHistoryRepository(ABC):
    @abstractmethod
    def addToStrategyHistory(self, request_id, aiResult):
        pass