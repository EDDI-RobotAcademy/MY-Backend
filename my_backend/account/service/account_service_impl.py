from account.repository.account_repository_impl import AccountRepositoryImpl
from account.service.account_service import AccountService
from user_profile.repository.user_profile_repository_impl import UserProfileRepositoryImpl


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__userProfileRepository = UserProfileRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def registerAccount(self, loginType, roleType, name, nickname, email):
        account = self.__accountRepository.create(loginType, roleType)
        return self.__userProfileRepository.create(name, nickname, email, account)

    def findAccountById(self, account_id):
        return self.__accountRepository.findById(account_id)