from abc import ABC, abstractmethod

class UserAnalysisRequestRepository(ABC):

    @abstractmethod
    def create(self, account_id, user_analysis_id):
        pass