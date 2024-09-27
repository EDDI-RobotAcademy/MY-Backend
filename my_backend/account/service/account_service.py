from abc import ABC, abstractmethod


class AccountService(ABC):

    @abstractmethod
    def registerAccount(self, loginType, roleType, nickname, email):
        pass
