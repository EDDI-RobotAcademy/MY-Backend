from abc import ABC, abstractmethod

class UserAnalysisRequestRepository(ABC):

    @abstractmethod
    def create(self, account_id, user_analysis_id, guest_identifier=None):
        pass

    @abstractmethod
    def list(self, account=None):
        pass

    @abstractmethod
    def findById(self, request_id):
        pass

    @abstractmethod
    def findByUserAnalysis(self, user_analysis):
        pass


    @abstractmethod
    def findLatestByAccount(self, account_id):
        pass

    @abstractmethod
    def findLatestByIdentifier(self, identifier):
        pass