from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kakao_pay.controller.views import KakaoPayView

router = DefaultRouter()
router.register(r'', KakaoPayView, basename='kakao_pay')

urlpatterns = [
    path('readyKakaoPay',KakaoPayView.as_view({'post': 'kakaoPayReady'}),name='readyKakaoPay'),
]