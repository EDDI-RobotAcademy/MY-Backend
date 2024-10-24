from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kakao_pay.controller.views import KakaoPayView

router = DefaultRouter()
router.register(r'kakao_pay', KakaoPayView, basename='kakao_pay')

urlpatterns = [
    path('readyKakaoPay',KakaoPayView.as_view({'post': 'kakaoPayReady'}),name='readyKakaoPay'),
    path('approveKakaoPay',KakaoPayView.as_view({'post': 'kakaoPayApprove'}),name='approveKakaoPay'),
]