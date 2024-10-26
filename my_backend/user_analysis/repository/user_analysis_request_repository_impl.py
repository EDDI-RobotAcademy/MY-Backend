from account.entity.account import Account
from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.entity.user_analysis_request import UserAnalysisRequest
from user_analysis.repository.user_analysis_request_repository import UserAnalysisRequestRepository


class UserAnalysisRequestRepositoryImpl(UserAnalysisRequestRepository):
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

    def create(self, account_id, user_analysis_id):
        account = Account.objects.get(id = account_id)
        user_analysis = UserAnalysis.objects.get(id = user_analysis_id)
        user_analysis_request = UserAnalysisRequest(account=account, user_analysis=user_analysis)
        user_analysis_request.save()

        return user_analysis_request

    def list(self, account=None):
        if account:
            return UserAnalysisRequest.objects.filter(account = account)
        else:
            return UserAnalysisRequest.objects.all()

    def findById(self, request_id):
        return UserAnalysisRequest.objects.get(id=request_id)


