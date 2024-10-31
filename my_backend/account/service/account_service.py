from abc import ABC, abstractmethod


class AccountService(ABC):

    @abstractmethod
    def registerAccount(self, loginType, roleType, name, nickname, email, membership):
        pass

    @abstractmethod
    def findAccountById(self, account_id):
        pass