from abc import ABC, abstractmethod

class UserAnalysisAnswerRepository(ABC):

    @abstractmethod
    def saveAnswer(self, question_id, answer_data):
        pass

    @abstractmethod
    def summarizeAnswerByUserAnalysisId(self, user_analysis_id):
        pass

    @abstractmethod
    def summarizeAnswerByQuestionId(self, question_id):
        pass

    @abstractmethod
    def summarizeAnswerByAccountId(self, account_id):
        pass

    @abstractmethod
    def summarizeAnswerByUserAnalysisIdandAccountId(self, user_analysis_id, account_id):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def findByRequest(self, request_id):
        pass