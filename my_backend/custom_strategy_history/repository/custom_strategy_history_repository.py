from abc import ABC, abstractmethod


class CustomStrategyHistoryRepository(ABC):
    @abstractmethod
    def addToStrategyHistory(self, request_id, aiResult):
        pass

    @abstractmethod
    def read(self, request_id):
        pass