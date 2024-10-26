from django.urls import path, include
from rest_framework.routers import DefaultRouter

from smart_content.controller.views import SmartContentView

router = DefaultRouter()
router.register(r'smart_content', SmartContentView, basename='smart_content')

urlpatterns = [
    path('', include(router.urls)),
    path('create', SmartContentView.as_view({'post': 'create'}), name='create-smart-content'),
    path('list', SmartContentView.as_view({'post': 'list'}), name='list-smart-content'),
]