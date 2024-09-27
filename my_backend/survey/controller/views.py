from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.entity.fixed_boolean_selection import FixedBooleanSelection
from survey.entity.fixed_five_score_selection import FixedFiveScoreSelection
from survey.entity.survey import Survey
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_question_image import SurveyQuestionImage
from survey.entity.survey_selection import SurveySelection
from survey.entity.survey_selection_image import SurveySelectionImage
from survey.entity.survey_type import SurveyType
from survey.service.survey_service_impl import SurveyServiceImpl

class SurveyView(viewsets.ViewSet):

    def create(self, request):
        print('controller -> createSurvey')
        print(Survey,
              SurveyType,
              SurveyQuestion,
              SurveyAnswer,
              SurveySelection,
              SurveyQuestionImage,
              SurveySelectionImage,
              FixedBooleanSelection,
              FixedFiveScoreSelection,
              )
