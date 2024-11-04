from django.urls import path, include
from rest_framework.routers import DefaultRouter

from keyword_search.controller.views import KeywordSearchView

router = DefaultRouter()
router.register(r'keyword_search', KeywordSearchView, basename='keyword_search')

urlpatterns = [
    path('', include(router.urls)),
    path('datalab',
         KeywordSearchView.as_view({'post': 'datalab_api'}),
         name='datalab'),
]
