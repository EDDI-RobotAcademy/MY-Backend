from abc import ABC, abstractmethod

class RedisService(ABC):
    @abstractmethod
    def storeAccessToken(self, userToken, user_data):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def deleteKey(self, key):
        pass