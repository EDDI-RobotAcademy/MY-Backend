from abc import ABC, abstractmethod

from survey.entity.survey_question import SurveyQuestion
from survey.entity.custom_selection import CustomSelection


class SurveySelectionRepository(ABC):

    @abstractmethod
    def createCustomSelection(self, question: SurveyQuestion, custom_text: str) -> CustomSelection:
        pass

    @abstractmethod
    def findCustomSelectionListByQuestionId(self, question_id):
        pass