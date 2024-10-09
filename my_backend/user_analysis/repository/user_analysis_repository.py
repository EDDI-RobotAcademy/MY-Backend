from abc import ABC, abstractmethod


class UserAnalysisRepository(ABC):
    @abstractmethod
    def create(self, title, description):
        pass
