from abc import ABC, abstractmethod


class UserProfileService(ABC):

    @abstractmethod
    def checkEmailDuplication(self, email):
        pass

    @abstractmethod
    def checkNicknameDuplication(self, nickname):
        pass

    @abstractmethod
    def findAccountByEmail(self, email):
        pass
