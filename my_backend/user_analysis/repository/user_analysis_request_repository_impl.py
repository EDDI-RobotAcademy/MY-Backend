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

    def create(self, account_id, user_analysis_id, guest_identifier=None):
        # 비회원일 경우 동일한 guest_identifier로 요청이 존재하는지 확인
        if guest_identifier is not None:
            existing_request = UserAnalysisRequest.objects.filter(guest_identifier=guest_identifier).order_by(
                '-created_at').first()
            if existing_request:
                # 기존 요청이 있다면 새로 생성하지 않고 반환
                return "duplicate_request"
        account = Account.objects.get(id = account_id) if account_id is not None else None
        user_analysis = UserAnalysis.objects.get(id = user_analysis_id)
        user_analysis_request = UserAnalysisRequest(
            account=account,
            user_analysis=user_analysis,
            guest_identifier=guest_identifier if account_id is None else None
        )
        user_analysis_request.save()

        return user_analysis_request

    def list(self, account=None):
        if account:
            return UserAnalysisRequest.objects.filter(account = account)
        else:
            return UserAnalysisRequest.objects.all()

    def findById(self, request_id):
        return UserAnalysisRequest.objects.get(id=request_id)

    def findByUserAnalysis(self, user_analysis):
        return UserAnalysisRequest.objects.filter(user_analysis = user_analysis)

    def findLatestByAccount(self, account_id):
        account = Account.objects.get(id = account_id)
        return UserAnalysisRequest.objects.filter(account = account).order_by('-created_at').first()

    def findLatestByIdentifier(self, identifier):
        return UserAnalysisRequest.objects.filter(guest_identifier = identifier).order_by('-created_at').first()
