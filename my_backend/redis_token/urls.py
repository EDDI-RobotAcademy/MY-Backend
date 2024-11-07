from django.urls import path, include
from rest_framework.routers import DefaultRouter
from redis_token.controller.views import RedisTokenView

router = DefaultRouter()
router.register(r'redis_token', RedisTokenView, basename='redis_token')

urlpatterns = [
    path('', include(router.urls)),
    path('create-member-token', RedisTokenView.as_view({'post': 'createMemberToken'}), name='redis-access-token'),
    path('logout', RedisTokenView.as_view({'post': 'dropRedisTokenForLogout'}), name='drop-redis-token-for-logout'),
    path('create-guest-token', RedisTokenView.as_view({'post': 'createGuestToken'}), name='create-guest-token'),
]