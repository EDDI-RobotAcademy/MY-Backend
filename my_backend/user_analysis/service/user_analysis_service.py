from abc import ABC, abstractmethod

class UserAnalysisService(ABC):
    @abstractmethod
    def createUserAnalysis(self, title, description):
        pass