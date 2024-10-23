from abc import ABC, abstractmethod


class UserProfileRepository(ABC):
    @abstractmethod
    def findByEmail(self, email):
        pass

    @abstractmethod
    def findByNickname(self, nickname):
        pass

    @abstractmethod
    def findByAccountId(self, accountId):
        pass

    @abstractmethod
    def create(self, name, nickname, email, account):
        pass

    @abstractmethod
    def findByIncompleteNickname(self, nickname):
        pass

    @abstractmethod
    def updateNickname(self, user_profile, new_nickname):
        pass



