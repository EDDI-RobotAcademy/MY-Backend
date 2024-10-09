from account.repository.account_repository_impl import AccountRepositoryImpl
from user_analysis.repository.user_analysis_question_repository_impl import UserAnalysisQuestionRepositoryImpl
from user_analysis.repository.user_analysis_repository_impl import UserAnalysisRepositoryImpl
from user_analysis.service.user_analysis_service import UserAnalysisService


class UserAnalysisServiceImpl(UserAnalysisService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__userAnalysisRepository = UserAnalysisRepositoryImpl.getInstance()
            cls.__instance.__userAnalysisQuestionRepository = UserAnalysisQuestionRepositoryImpl.getInstance()

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

    def createUserAnalysisQuestion(self, user_analysis_id, question_text, user_analysis_type):
        user_analysis = self.__userAnalysisRepository.findById(user_analysis_id)
        if user_analysis is None:
            raise ValueError("UserAnalysis not found")

        return self.__userAnalysisQuestionRepository.create(user_analysis, question_text, user_analysis_type)