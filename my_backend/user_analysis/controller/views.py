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