from my_backend import settings
from kakao_pay.service.kakao_pay_service import KakaoPayService
import requests


class KakaoPayServiceImpl(KakaoPayService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.key = settings.KAKAO_PAY['KEY']
            cls.__instance.host = settings.KAKAO_PAY['HOST']
            cls.__instance.cid = settings.KAKAO_PAY['CID']
            cls.__instance.partnerOrderPrefix = settings.KAKAO_PAY['PARTNER_ORDER_PREFIX']
            cls.__instance.partnerUserId = settings.KAKAO_PAY['PARTNER_USER_ID']
            cls.__instance.redirectUri = settings.KAKAO_PAY['REDIRECT_URI']
            cls.__instance.approvalUrl = settings.KAKAO_PAY['APPROVAL_URL']
            cls.__instance.failUrl = settings.KAKAO_PAY['FAIL_URL']
            cls.__instance.cancelUrl = settings.KAKAO_PAY['CANCEL_URL']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def kakaoPayReadyAddress(self, amount):
        print("kakaoPayAddress()")
        headers = {
            'Authorization': "KakaoAK " + self.key,
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
        }
        url = f"{self.host}/v1/payment/ready"
        params = {
            "cid": self.cid,
            "partner_order_id": self.partnerOrderPrefix,
            "partner_user_id": self.partnerUserId,
            "item_name": "포인트",
            "quantity": 1,
            "total_amount": amount,
            "vat_amount": 200,
            "tax_free_amount": 0,
            "approval_url": self.approvalUrl,
            "fail_url": self.failUrl,
            "cancel_url": self.cancelUrl
        }

        response = requests.post(url, data=params, headers=headers)
        print("response 출력", url)
        return response.json()