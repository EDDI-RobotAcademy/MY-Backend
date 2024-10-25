from rest_framework import viewsets, status
from rest_framework.response import Response
from django.conf import settings
import requests
import uuid
import logging
import base64

logger = logging.getLogger(__name__)


class TosspaymentsView(viewsets.ViewSet):
    def create_payment(self, request):
        try:
            amount = 50000
            order_name = "토스 티셔츠 외 2건"
            customer_email = "customer123@gmail.com"
            customer_name = "김토스"
            customer_mobile_phone = "01012341234"

            order_id = str(uuid.uuid4())

            payment_data = {
                'amount': amount,
                'orderId': order_id,
                'orderName': order_name,
                'successUrl': f"{settings.TOSS_PAY_BASE_URL}/api/v1/payments/success",
                'failUrl': f"{settings.TOSS_PAY_BASE_URL}/api/v1/payments/fail",
                'customerEmail': customer_email,
                'customerName': customer_name,
                'customerMobilePhone': customer_mobile_phone,
            }

            return Response({
                'status': 'success',
                'data': payment_data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"[Payment Create] Error: {str(e)}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

    def payment_success(self, request):
        try:
            data = request.data
            print("data", data)
            payment_key = data.get('paymentKey')
            print("paymentKey", payment_key)
            order_id = data.get('orderId')
            print("orderId", order_id)
            amount = data.get('amount')
            print("amount", amount)

            if not all([payment_key, order_id, amount]):
                return Response({
                    'error': 'Missing required parameters'
                }, status=status.HTTP_400_BAD_REQUEST)

            url = "https://api.tosspayments.com/v1/payments/confirm"

            secret_key = settings.TOSS_PAYMENTS_SECRET_KEY
            basic_auth = f"{secret_key}:"
            basic_auth_bytes = basic_auth.encode('utf-8')
            basic_auth_base64 = base64.b64encode(basic_auth_bytes).decode('utf-8')

            headers = {
                'Authorization': f'Basic {basic_auth_base64}',
                'Content-Type': 'application/json'
            }

            response = requests.post(url,
                                     json={
                                         'paymentKey': payment_key,
                                         'orderId': order_id,
                                         'amount': amount
                                     },
                                     headers=headers
                                     )

            print("Toss API Response:", response.text)
            return Response(response.json(), status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({
                'error': 'Payment confirmation failed',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
