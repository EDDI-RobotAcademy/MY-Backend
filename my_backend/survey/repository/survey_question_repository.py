from abc import ABC, abstractmethod

class SurveyQuestionRepository(ABC):
    @abstractmethod
    def create(self, survey, question_text, survey_type):
        pass
