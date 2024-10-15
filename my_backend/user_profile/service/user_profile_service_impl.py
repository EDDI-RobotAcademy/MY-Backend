from account.repository.account_repository_impl import AccountRepositoryImpl
from user_profile.repository.user_profile_repository_impl import UserProfileRepositoryImpl
from user_profile.service.user_profile_service import UserProfileService


class UserProfileServiceImpl(UserProfileService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userProfileRepository = UserProfileRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def checkEmailDuplication(self, email):
        profile = self.__userProfileRepository.findByEmail(email)
        return profile is not None

    def checkNicknameDuplication(self, nickname):
        profile = self.__userProfileRepository.findByNickname(nickname)
        return profile is not None

    def findAccountByEmail(self, email):
        return self.__userProfileRepository.findByEmail(email)


