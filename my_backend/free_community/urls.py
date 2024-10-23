from django.urls import path, include
from rest_framework.routers import DefaultRouter

from free_community.controller.views import FreeCommunityView

router = DefaultRouter()
router.register(r'free_community', FreeCommunityView)

urlpatterns = [
    path('', include(router.urls)),
    path('get-allcontent', FreeCommunityView.as_view({'get': 'list'}), name='free_community-list'),
    path('list-by-category', FreeCommunityView.as_view({'post': 'listByCategory'}), name='list-by-category'),
    path('list-by-title', FreeCommunityView.as_view({'get': 'listByTitle'}), name='list-by-title'),
    path('list-by-content', FreeCommunityView.as_view({'get': 'listByContent'}), name='list-by-content'),
    path('list-by-nickname', FreeCommunityView.as_view({'get': 'listByNickname'}), name='list-by-nickname'),
    path('register', FreeCommunityView.as_view({'post': 'create'}), name='free_community-register'),
    path('create-category', FreeCommunityView.as_view({'post': 'createCategory'}), name='create-category'),
    path('get-categories', FreeCommunityView.as_view({'get': 'getCategories'}), name='get-categories'),
    path('read/<int:pk>', FreeCommunityView.as_view({'get': 'readFreeCommunity'}), name='free_community-read'),
    path('delete/<int:pk>', FreeCommunityView.as_view({'delete': 'removeFreeCommunity'}), name='free_community-remove'),
    path('modify/<int:pk>', FreeCommunityView.as_view({'put': 'modifyFreeCommunity'}), name='free_community-modify'),
    path('check-authority/<int:pk>', FreeCommunityView.as_view({'post': 'checkAuthority'}), name='check-authority'),
]