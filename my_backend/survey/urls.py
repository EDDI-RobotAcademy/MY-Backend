from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.controller.views import SurveyView

router = DefaultRouter()
router.register(r'survey', SurveyView, basename='survey')

urlpatterns = [
    path('', include(router.urls)),
    path('create', SurveyView.as_view({'post': 'createSurvey'}), name='create-survey'),
    path('create-question', SurveyView.as_view({'post': 'createSurveyQuestion'}), name='create-survey-question'),
    path('create-selection', SurveyView.as_view({'post': 'createCustomSelection'}), name='create-custom-selection'),
    path('submit-answer', SurveyView.as_view({'post': 'submitSurveyAnswer'}), name='submit-survey-answer'),
    path('list-answer', SurveyView.as_view({'post': 'listSurveyAnswer'}), name='list-survey-answer')
]