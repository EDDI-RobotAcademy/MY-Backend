from smart_content.repository.smart_content_repository_impl import SmartContentRepositoryImpl
from smart_content.service.smart_content_service import SmartContentService


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

    def list(self):
        return self.__smartContentRepository.list()

    def listItems(self, contentId):
        return self.__smartContentRepository.listItems(contentId)

    def read(self, contentId):
        return self.__smartContentRepository.findByContentId(contentId)