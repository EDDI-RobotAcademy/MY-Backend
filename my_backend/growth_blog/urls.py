from django.urls import path, include
from rest_framework.routers import DefaultRouter

from growth_blog.controller.views import GrowthBlogView

router = DefaultRouter()
router.register(r'growth_blog', GrowthBlogView, basename='growth_blog')

urlpatterns = [
    path('', include(router.urls)),
    path('following', GrowthBlogView.as_view({'post': 'followingByNickname'}), name='following'),
    path('registerSocial', GrowthBlogView.as_view({'post': 'registerFollowingAndFollowers'}), name='registerSocial'),
]