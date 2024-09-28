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
    surveyService = SurveyServiceImpl.getInstance()

    def createSurvey(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')

        if not title:
            return Response({"error": "제목이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        isCreated = {"title": f"{self.surveyService.createSurvey(title, description)}"}

        return Response(isCreated, status=status.HTTP_200_OK)

    def createSurveyQuestion(self, request):
        data = request.data
        survey_id = data.get('survey')
        question_text = data.get('question')
        survey_type = data.get('survey_type')

        if not survey_id or not question_text:
            return Response({"error": "설문 ID와 질문 내용이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            self.surveyService.createSurveyQuestion(survey_id, question_text, survey_type)
            return Response({"success": "질문이 추가되었습니다"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)



