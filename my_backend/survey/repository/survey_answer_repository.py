from abc import ABC, abstractmethod

class SurveyAnswerRepository(ABC):
    @abstractmethod

    def saveAnswer(self, survey_id, question_id, answer_data, account_id):
        pass



