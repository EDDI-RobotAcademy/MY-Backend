from django.urls import include, path
from rest_framework.routers import DefaultRouter
from viewCount.controller.views import ViewCountView

router = DefaultRouter()
router.register(r'viewCount', ViewCountView, basename='viewCount')

urlpatterns = [
    path('increment-count/<int:pk>', ViewCountView.as_view({'post': 'increment_community'}), name='increment_count'),
]