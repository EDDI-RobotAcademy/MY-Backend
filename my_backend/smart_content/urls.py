from django.urls import path, include
from rest_framework.routers import DefaultRouter

from smart_content.controller.views import SmartContentView

router = DefaultRouter()
router.register(r'smart_content', SmartContentView, basename='smart_content')

urlpatterns = [
    path('', include(router.urls)),
    path('create', SmartContentView.as_view({'post': 'create'}), name='create-smart-content'),
    path('list', SmartContentView.as_view({'post': 'list'}), name='list-smart-content'),
    path('list-items', SmartContentView.as_view({'post': 'listItems'}), name='list-smart-content-items'),
    path('read/<int:pk>', SmartContentView.as_view({'get': 'read'}), name='read-smart-content'),
    path('list-self', SmartContentView.as_view({'post': 'listByAccountId'}), name='list-self-content'),
]