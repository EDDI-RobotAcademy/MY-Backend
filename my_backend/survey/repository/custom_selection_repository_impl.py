from django.db import IntegrityError

from survey.entity.survey_question import SurveyQuestion
from survey.entity.custom_selection import CustomSelection
from survey.repository.custom_selection_repository import SurveySelectionRepository


class CustomSelectionRepositoryImpl(SurveySelectionRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createCustomSelection(self, question, custom_text):
        if not isinstance(question, SurveyQuestion):
            raise ValueError("Question must be an instance of SurveyQuestion")

        try:
            selection = CustomSelection(question=question, custom_text=custom_text)
            selection.save()
            return selection

        except IntegrityError as e:
            raise IntegrityError(f"Error creating survey selection: {e}")



