from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serilaizers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from ai_request.service.ai_request_service_impl import AiRequestServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
from user_analysis.repository.user_analysis_request_repository_impl import UserAnalysisRequestRepositoryImpl
from user_analysis.service.user_analysis_service_impl import UserAnalysisServiceImpl


class AiRequestView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    aiRequestService = AiRequestServiceImpl.getInstance()
    userAnalysisService = UserAnalysisServiceImpl.getInstance()
    userAnalysisRequestRepository = UserAnalysisRequestRepositoryImpl.getInstance()

    def aiRequestToFastAPI(self, request):
        command = request.data.get('command')
        userToken = request.data.get('userToken')

        if userToken:
            user_identifier = self.redisService.getValueByKey(userToken)
            print("user_identifier: ", user_identifier)

            # account_id가 int 타입인 경우 회원, str 타입인 경우 비회원
            if isinstance(user_identifier, int):
                account_id = user_identifier
                guest_identifier = None
            else:
                account_id = None
                guest_identifier = user_identifier  # 비회원의 경우 IP 주소
        else:
            account_id = None
            guest_identifier = None

        if account_id is not None:
            # 회원일 경우 findLatestByAccount 호출
            user_analysis_request = self.userAnalysisRequestRepository.findLatestByAccount(account_id)
        else:
            # 비회원일 경우 findLatestByIdentifier 호출
            user_analysis_request = self.userAnalysisRequestRepository.findLatestByIdentifier(guest_identifier)

        if not user_analysis_request:
            return Response({"error": "No analysis request found for the user."}, status=status.HTTP_404_NOT_FOUND)


        data = self.userAnalysisService.getAnswer(user_analysis_request.id)
        data.append(userToken)
        data.append(user_analysis_request.id)

        requestComplete = self.aiRequestService.aiRequestToFastAPI(command, data)

        # 추후 account 별 구독 유형 확인해서 구분하는 작업 필요
        # subscription_type = serializer.data.get('roleType') # 임시로 roleType으로 지정 -> 추후 변경 필요
        # if subscription_type == "ADMIN":    # 임시로 roleType으로 지정 -> 추후 변경 필요
        #     requestComplete = self.aiRequestService.aiRequestToFastAPI(userToken, command, data)
        # else:
        #     requestComplete = False
        #     print("AI 요청 권한이 없는 사용자입니다.")

        return Response(requestComplete, status=status.HTTP_200_OK)

