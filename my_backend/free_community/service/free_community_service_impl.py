from free_community.repository.free_community_repository_impl import FreeCommunityRepositoryImpl
from free_community.service.free_community_service import FreeCommunityService
from user_profile.repository.user_profile_repository_impl import UserProfileRepositoryImpl


class FreeCommunityServiceImpl(FreeCommunityService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__free_communityRepository = FreeCommunityRepositoryImpl.getInstance()
            cls.__instance.__userProfileRepository = UserProfileRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__free_communityRepository.list()

    def createCategory(self, name):
        return self.__free_communityRepository.create_category(name)

    def createFreeCommunity(self, categoryId, title, accountId, content, contentImage, is_notice=False):
        return self.__free_communityRepository.create(categoryId, title, accountId, content, contentImage, is_notice)

    def readFreeCommunity(self, free_communityId):
        return self.__free_communityRepository.findByFreeCommunityId(free_communityId)

    def removeFreeCommunity(self, free_communityId):
        return self.__free_communityRepository.deleteByFreeCommunityId(free_communityId)

    def updateFreeCommunity(self, free_communityId, free_communityData):
        free_community = self.__free_communityRepository.findByFreeCommunityId(free_communityId)
        return self.__free_communityRepository.update(free_community, free_communityData)

    def get_all_categories(self):
        return list(self.__free_communityRepository.get_all_categories())

    def listByCategoryId(self, categoryId):
        return self.__free_communityRepository.listFreeCommunityByCategoryId(categoryId)

    def listByTitle(self, title):
        return self.__free_communityRepository.listFreeCommunityByTitle(title)

    def listByContent(self, content):
        return self.__free_communityRepository.listFreeCommunityByContent((content))

    def listByNickname(self, nickname):
        profiles = self.__userProfileRepository.findByIncompleteNickname(nickname)
        if profiles.exists():
            free_communitys=[]
            for profile in profiles:
                account_free_communitys = self.__free_communityRepository.listFreeCommunityByAccount(profile.account)
                free_communitys.extend(account_free_communitys)

            return free_communitys

    def getNotices(self):
        return self.__free_communityRepository.listNotices()





