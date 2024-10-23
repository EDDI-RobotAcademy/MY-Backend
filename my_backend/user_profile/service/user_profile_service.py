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

    @abstractmethod
    def changeNickname(self, account_id, new_nickname):
        pass

    @abstractmethod
    def getNicknameByAccountId(self, account_id):
        pass

    @abstractmethod
    def getUserProfileByAccountId(self, account_id):
        pass

    @abstractmethod
    def getUserProfileByNickname(self, nickname):
        pass