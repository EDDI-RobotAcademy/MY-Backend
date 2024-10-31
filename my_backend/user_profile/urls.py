from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_profile.controller.views import UserProfileView

router = DefaultRouter()
router.register(r'user_profile', UserProfileView, basename='user_profile')

urlpatterns = [
    path('', include(router.urls)),
    path('email-duplication-check',
         UserProfileView.as_view({'post': 'checkEmailDuplication'}),
         name='profile-email-duplication-check'),
    path('nickname-duplication-check',
         UserProfileView.as_view({'post': 'checkNicknameDuplication'}),
         name='profile-nickname-duplication-check'),
    path('register',
         UserProfileView.as_view({'post': 'registerProfile'}),
         name='register-profile'),
    path('get-nickname', UserProfileView.as_view({'post': 'getNickname'}), name='get-profile-nickname'),
    path('change-nickname', UserProfileView.as_view({'put': 'changeNickname'}), name='change-nickname'),
    path('get-self-profile', UserProfileView.as_view({'post': 'getUserProfileByAccountId'}), name='get-self-profile'),
    path('get-profile', UserProfileView.as_view({'post': 'getUserProfileByNickname'}), name='get-profile'),
    path('nickname-by-accountid', UserProfileView.as_view({'post': 'getUserByAccountId'}), name='nickname-by-accountid'),
    path('change-membership', UserProfileView.as_view({'put': 'changeMembership'}), name='change-membership'),

]
