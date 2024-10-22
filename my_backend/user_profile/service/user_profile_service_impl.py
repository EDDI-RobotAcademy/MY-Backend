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

    def changeNickname(self, account_id, new_nickname):
        user_profile = self.__userProfileRepository.findByAccountId(account_id)
        print(f"찾은 사용자 프로필: {user_profile}")

        updated_nickname = self.__userProfileRepository.updateNickname(user_profile, new_nickname)
        print(f"닉네임 업데이트 성공: {updated_nickname.nickname}")
        return updated_nickname

