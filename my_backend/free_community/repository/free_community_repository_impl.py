from account.entity.account import Account
from free_community.entity.FreeCommunityCategory import FreeCommunityCategory
from free_community.entity.models import FreeCommunity
from free_community.repository.free_community_repository import FreeCommunityRepository


class FreeCommunityRepositoryImpl(FreeCommunityRepository):
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

    def list(self):
        return FreeCommunity.objects.all().order_by('regDate')

    def create_category(self, name):
        category = FreeCommunityCategory(**name)
        category.save()
        return category

    def create(self, categoryId, title, accountId, content, contentImage, is_notice=False):
        if accountId:
            account = Account.objects.get(id=accountId)
        else:
            account = None
        category = FreeCommunityCategory.objects.get(categoryId=categoryId)

        free_community = FreeCommunity(
            category = category,
            title = title,
            account = account,
            content = content,
            contentImage = contentImage,
            is_notice=is_notice
        )
        free_community.save()
        return free_community

    def findByFreeCommunityId(self, free_communityId):
        return FreeCommunity.objects.get(free_communityId=free_communityId)

    def deleteByFreeCommunityId(self, free_communityId):
        free_community = FreeCommunity.objects.get(free_communityId=free_communityId)
        free_community.delete()

    def update(self, free_community, free_communityData):
        for key, value in free_communityData.items():
            print(f"key: {key}, value: {value}")
            setattr(free_community, key, value)
        free_community.save()
        return free_community

    def get_all_categories(self):
        return FreeCommunityCategory.objects.all().order_by('categoryId').values('categoryId', 'name')

    def listFreeCommunityByCategoryId(self, categoryId):
        return FreeCommunity.objects.filter(category=categoryId)

    def listFreeCommunityByTitle(self, title):
        return FreeCommunity.objects.filter(title__icontains=title)

    def listFreeCommunityByContent(self, content):
        return FreeCommunity.objects.filter(content__icontains=content)

    def listFreeCommunityByAccount(self, account):
        return FreeCommunity.objects.filter(account=account)

    def listNotices(self):
        return FreeCommunity.objects.filter(is_notice=True).order_by('-regDate').values()