from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_analysis.controller.views import UserAnalysisView

router = DefaultRouter()
router.register(r'user_analysis', UserAnalysisView, basename='user_analysis')

urlpatterns = [
    path('', include(router.urls)),
    path('create', UserAnalysisView.as_view({'post': 'createUserAnalysis'}), name='create-user-analysis'),
    path('create-question', UserAnalysisView.as_view({'post': 'createUserAnalysisQuestion'}), name='create-user-analysis-question'),

]