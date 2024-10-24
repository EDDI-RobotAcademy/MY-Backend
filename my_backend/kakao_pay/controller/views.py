from rest_framework import viewsets
from rest_framework.response import Response
from kakao_pay.service.kakao_pay_service_impl import KakaoPayServiceImpl


class KakaoPayView(viewsets.ViewSet):
    kakao_payService = KakaoPayServiceImpl.getInstance()

    def kakaoPayReady(self, request):
        amount = request.data.get('amount')
        result = self.kakao_payService.kakaoPayReadyAddress(amount)
        return Response(result)

    def kakaoPayApprove(self, request):
        try:
            tid = request.data.get('tid')
            pg_token = request.data.get('pg_token')
            print("tid 출력", tid)
            print("pg_token 출력", pg_token)
            if not tid or not pg_token:
                return Response({
                    'error': '필수 파라미터가 누락되었습니다.'
                }, status=400)

            result = self.kakao_payService.kakaoPayApproveDone(tid, pg_token)
            return Response(result)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=500)
