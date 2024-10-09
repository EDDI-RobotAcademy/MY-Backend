from rest_framework import viewsets, status
from rest_framework.response import Response

from user_analysis.service.user_analysis_service_impl import UserAnalysisServiceImpl


class UserAnalysisView(viewsets.ViewSet):
    userAnalysisService = UserAnalysisServiceImpl.getInstance()

    def createUserAnalysis(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')

        if not title:

            return Response({"error": "제목이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        isCreated = {"title": f"{self.userAnalysisService.createUserAnalysis(title, description)}"}

        return Response(isCreated, status=status.HTTP_200_OK)

    def createUserAnalysisQuestion(self, request):
        data = request.data
        user_analysis_id = data.get('user_analysis')
        question_text = data.get('question')
        user_analysis_type = data.get('user_analysis_type')

        if not user_analysis_id or not question_text:
            return Response({"error": "유저조사 ID와 질문 내용이 필요합니다"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            question = self.userAnalysisService.createUserAnalysisQuestion(user_analysis_id, question_text, user_analysis_type)
            return Response({"success": "질문이 추가되었습니다", "questionId": f"{question.id}"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)