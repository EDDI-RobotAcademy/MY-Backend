from user_profile.entity.user_profile import UserProfile
from user_profile.repository.user_profile_repository import UserProfileRepository


class UserProfileRepositoryImpl(UserProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = UserProfile.objects.get(email=email)
            return profile
        except UserProfile.DoesNotExist:
            print(f"email로 profile을 찾을 수 없습니다.: {email}")
            return None
        except Exception as e:
            print(f"error occurred during email duplicate check: {e}")
            return None

    def findByNickname(self, nickname):
        try:
            profile = UserProfile.objects.get(nickname=nickname)
            return profile
        except UserProfile.DoesNotExist:
            print(f"nickname으로 profile을 찾을 수 없습니다.: {nickname}")
            return None
        except Exception as e:
            print(f"error occurred during nickname duplicate check: {e}")
            return None

    def findByAccountId(self, accountId):
        profile = UserProfile.objects.get(account=accountId)
        return profile

    def create(self, name, nickname, email, account):
        profile = UserProfile.objects.create(name = name, nickname=nickname, email=email, account=account)
        return profile

    def findByIncompleteNickname(self, nickname):
        try:
            profiles = UserProfile.objects.filter(nickname__icontains=nickname)
            print(f"profile: {profiles}")
            return profiles
        except UserProfile.DoesNotExist:
            print(f"nickname으로 profile을 찾을 수 없습니다.: {nickname}")
            return None
        except Exception as e:
            print(f"error occurred during nickname duplicate check: {e}")
            return None


