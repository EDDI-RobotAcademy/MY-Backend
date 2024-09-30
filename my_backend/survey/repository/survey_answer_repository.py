from abc import ABC, abstractmethod

class SurveyAnswerRepository(ABC):
    @abstractmethod
    def saveAnswer(self, survey, question, answer_data, account):
        pass



