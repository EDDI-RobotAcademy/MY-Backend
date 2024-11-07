from django.urls import path, include
from rest_framework.routers import DefaultRouter

from like_count.controller.views import LikeCountView

router = DefaultRouter()
router.register(r'like_count', LikeCountView, basename='like_count')

urlpatterns = [
    path('', include(router.urls)),
    path('toggle-like', LikeCountView.as_view({'post': 'toggleLike'}), name='toggle-like'),
    path('count-like', LikeCountView.as_view({'post': 'getLikeCount'}), name='count-like'),
]