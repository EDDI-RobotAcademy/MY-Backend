from abc import ABC, abstractmethod

class UserAnalysisAnswerRepository(ABC):

    @abstractmethod
    def saveAnswer(self, user_analysis_id, question_id, answer_data, account_id):
        pass