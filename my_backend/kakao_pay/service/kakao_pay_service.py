from abc import ABC, abstractmethod


class KakaoPayService(ABC):
    @abstractmethod
    def kakaoPayReadyAddress(self, amount):
        pass

    @abstractmethod
    def kakaoPayApproveDone(self, tid, pg_token):
        pass

