from smart_content.repository.smart_content_repository_impl import SmartContentRepositoryImpl
from smart_content.service.smart_content_service import SmartContentService
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



class SmartContentServiceImpl(SmartContentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__smartContentRepository = SmartContentRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def create(self, title, content_type, items, nickname, accountId):
        return self.__smartContentRepository.create(title, content_type, items, nickname, accountId)

    def list(self, page_number=1, items_per_page=6):
        smartContentList = self.__smartContentRepository.list()
        paginator = Paginator(smartContentList, items_per_page)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            return []

        return page_obj.object_list

    def listByAccountId(self, accountId, page_number=1, items_per_page=6):
        smartContentList = self.__smartContentRepository.findByAccountId(accountId)

        paginator = Paginator(smartContentList, items_per_page)

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            return []

        return page_obj.object_list

    def listItems(self, contentId):
        return self.__smartContentRepository.listItems(contentId)

    def read(self, contentId):
        return self.__smartContentRepository.findByContentId(contentId)