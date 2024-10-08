from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from survey.entity.fixed_boolean_selection import FixedBooleanSelection
from survey.entity.fixed_five_score_selection import FixedFiveScoreSelection
from survey.entity.survey import Survey
from survey.entity.survey_answer import SurveyAnswer
from survey.entity.survey_question import SurveyQuestion
from survey.entity.survey_question_image import SurveyQuestionImage
from survey.entity.custom_selection import CustomSelection
from survey.entity.custom_selection_image import CustomSelectionImage
from survey.entity.survey_type import SurveyType
from survey.repository.survey_question_repository_impl import SurveyQuestionRepositoryImpl
from survey.serilaizers import SurveyAnswerSerializer, SurveyQuestionSerializer, CustomSelectionSerializer, \
    FixedBooleanSelectionSerializer, FixedFiveScoreSelectionSerializer, SurveySerializer
from survey.service.survey_service_impl import SurveyServiceImpl

class SurveyView(viewsets.ViewSet):
    surveyService = SurveyServiceImpl.getInstance()
    surveyQuestionRepository = SurveyQuestionRepositoryImpl.getInstance()

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
            question = self.surveyService.createSurveyQuestion(survey_id, question_text, survey_type)
            return Response({"success": "질문이 추가되었습니다", "questionId": f"{question.id}"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def createCustomSelection(self, request):
        try:
            data = request.data
            question_id = data.get('question_id')
            custom_text = data.get('custom_text')
            print(f"question_id: {question_id}, selection_text: {custom_text}")

            if not question_id or not custom_text:
                return Response({"error": "Question ID and selection text are required."},
                                status=status.HTTP_400_BAD_REQUEST)

            selection = self.surveyService.createSurveySelection(question_id, custom_text)

            return Response({"message": "Selection created successfully", "selection_id": selection.id},
                            status=status.HTTP_201_CREATED)

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "Something went wrong while creating the selection."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def submitSurveyAnswer(self, request):
        try:
            answers = request.data.get('survey_answer')
            accountId = request.data.get('account_id')
            print(f"answers: {answers}, accountId : {accountId}")

            self.surveyService.saveAnswer(answers, accountId)

            return Response(True, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)


    def listSurveyAnswer(self, request):
        try:
            filter = request.data.get('filter')
            surveyId = request.data.get("survey_Id")
            questionId = request.data.get("question_Id")
            accountId = request.data.get("account_Id")

            print(f"filter: {filter}, surveyId: {surveyId}, questionId: {questionId}, accountId: {accountId}")

            listedAnswer = self.surveyService.listAnswer(filter, surveyId, questionId, accountId)

            serializer = SurveyAnswerSerializer(listedAnswer, many=True)

            return Response(serializer.data, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def listSurveyQuestion(self, request):
        try:
            surveyId = request.data.get('survey_Id')

            print(f"surveyId: {surveyId}")

            listedQuestions = self.surveyService.listQuestions(surveyId)

            serializer = SurveyQuestionSerializer(listedQuestions, many=True)
            print(serializer)

            return Response(serializer.data, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def listSurveySelection(self, request):
        try:
            questionId = request.data.get('question_Id')
            print(f"questionId: {questionId}")

            listedSelections = self.surveyService.listSelections(questionId)
            print(f"listedSelections: {listedSelections}")

            question = self.surveyQuestionRepository.findById(questionId)
            print(question.survey_type)
            if question.survey_type == 1:
                return Response({"message": "This is a descriptive question, no choices available."},
                                status=status.HTTP_200_OK)

            if question.survey_type == 2:
                serializer = FixedFiveScoreSelectionSerializer(listedSelections, many=True)
            elif question.survey_type == 3:
                serializer = FixedBooleanSelectionSerializer(listedSelections, many=True)
            elif question.survey_type == 4:
                serializer = CustomSelectionSerializer(listedSelections, many=True)
            else:
                return Response({"error": "Invalid survey type"}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def listSurvey(self, request):
        surveyList = self.surveyService.listSurvey()
        serializer = SurveySerializer(surveyList, many=True)
        return Response(serializer.data)




