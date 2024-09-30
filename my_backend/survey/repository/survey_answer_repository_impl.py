from survey.entity.custom_selection import CustomSelection
from survey.entity.fixed_boolean_selection import FixedBooleanSelection
from survey.entity.fixed_five_score_selection import FixedFiveScoreSelection
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_selection import SurveySelection
from survey.repository.survey_answer_repository import SurveyAnswerRepository
from django.db import IntegrityError

class SurveyAnswerRepositoryImpl(SurveyAnswerRepository):
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

    def saveAnswer(self, survey, question, answer_data, account):
        if not isinstance(question, SurveyQuestion):
            raise ValueError("Question must be an instance of SurveyQuestion")
        try:
            if question.survey_type == 1: # General
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    answer_text=answer_data.get('answer'),
                    account=account
                ),
            elif question.survey_type == 2: # Five Score
                five_score_selection = FixedFiveScoreSelection.objects.get(id=answer_data.get('answer'))
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    five_score_selection=five_score_selection,
                    account=account
                ),
            elif question.survey_type == 3: # Boolean
                boolean_selection = FixedBooleanSelection.objects.get(is_true=answer_data.get('answer'))
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    boolean_selection=boolean_selection,
                    account=account
                )
            elif question.survey_type == 4:  # Custom
                custom_selection = SurveySelection.objects.get(id=answer_data.get('answer'))
                answer = SurveyAnswer(
                    survey=survey,
                    question=question,
                    custom_selection=custom_selection,
                    account=account
                )

            answer.save()
            return answer

        except IntegrityError as e:
            raise IntegrityError(f"Error saving survey answer: {e}")

