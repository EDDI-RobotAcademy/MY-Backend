from abc import ABC, abstractmethod


class KakaoPayService(ABC):
    @abstractmethod
    def kakaoPayReadyAddress(self, amount):
        pass

