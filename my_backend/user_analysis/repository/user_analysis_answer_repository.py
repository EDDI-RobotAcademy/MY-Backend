from abc import ABC, abstractmethod

class UserAnalysisAnswerRepository(ABC):

    @abstractmethod
    def saveAnswer(self, user_analysis_id, question_id, answer_data, account_id):
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