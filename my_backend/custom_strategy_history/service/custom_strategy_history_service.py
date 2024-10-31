from abc import ABC, abstractmethod


class CustomStrategyHistoryService(ABC):
    @abstractmethod
    def saveStrategyData(self, request_id, aiResult):
        pass