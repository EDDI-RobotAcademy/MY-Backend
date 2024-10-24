from rest_framework import viewsets
import requests
from rest_framework.response import Response
from kakao_pay.serializer.kakao_pay_url_serializer import KakaoPayUrlSerializer
from kakao_pay.service.kakao_pay_service_impl import KakaoPayServiceImpl


class KakaoPayView(viewsets.ViewSet):
    kakao_payService = KakaoPayServiceImpl.getInstance()

    def kakaoPayReady(self, request):
        amount = request.data.get('amount')
        result = self.kakao_payService.kakaoPayReadyAddress(amount)
        return Response(result)