from django.urls import path, include
from rest_framework.routers import DefaultRouter

from survey.controller.views import SurveyView

router = DefaultRouter()
router.register(r'survey', SurveyView, basename='survey')

urlpatterns = [
    path('', include(router.urls)),
]