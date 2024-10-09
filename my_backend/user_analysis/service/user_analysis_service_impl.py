from account.repository.account_repository_impl import AccountRepositoryImpl
from user_analysis.repository.user_analysis_repository_impl import UserAnalysisRepositoryImpl
from user_analysis.service.user_analysis_service import UserAnalysisService


class UserAnalysisServiceImpl(UserAnalysisService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userAnalysisRepository = UserAnalysisRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createUserAnalysis(self, title, description):
        try:
            return self.__userAnalysisRepository.create(title, description)

        except Exception as e:
            print('Error creating order:', e)
            raise e