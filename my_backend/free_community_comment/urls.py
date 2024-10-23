from django.urls import path, include
from rest_framework.routers import DefaultRouter

from free_community_comment.controller.views import FreeCommunityCommentView
from free_community_comment.entity.models import FreeCommunityComment

router = DefaultRouter()
router.register(r'free_community_comment', FreeCommunityCommentView, basename='free_community_comment')

urlpatterns = [
    path('', include(router.urls)),
    path('list-comment', FreeCommunityCommentView.as_view({'post': 'listComments'}), name='comment-list'),
    path('list-replies', FreeCommunityCommentView.as_view({'post': 'listReplies'}), name='reply-list'),
    path('create', FreeCommunityCommentView.as_view({'post': 'createComment'}), name='create-comment'),
    path('read/<int:pk>', FreeCommunityCommentView.as_view({'get': 'readComments'}), name='comment-read'),
]