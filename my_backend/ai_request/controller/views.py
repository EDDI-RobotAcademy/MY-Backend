from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serilaizers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from ai_request.service.ai_request_service_impl import AiRequestServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
from user_analysis.service.user_analysis_service_impl import UserAnalysisServiceImpl


class AiRequestView(viewsets.ViewSet):
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    aiRequestService = AiRequestServiceImpl.getInstance()
    userAnalysisService = UserAnalysisServiceImpl.getInstance()

    def aiRequestToFastAPI(self, request):
        data = request.data
        userToken = data.get('userToken')
        command = data.get('command')
        request_id = data.get('request_id')

        data = self.userAnalysisService.getAnswer(request_id)

        requestComplete = self.aiRequestService.aiRequestToFastAPI(userToken, command, request_id, data)

        # 추후 account 별 구독 유형 확인해서 구분하는 작업 필요
        # subscription_type = serializer.data.get('roleType') # 임시로 roleType으로 지정 -> 추후 변경 필요
        # if subscription_type == "ADMIN":    # 임시로 roleType으로 지정 -> 추후 변경 필요
        #     requestComplete = self.aiRequestService.aiRequestToFastAPI(userToken, command, data)
        # else:
        #     requestComplete = False
        #     print("AI 요청 권한이 없는 사용자입니다.")

        return Response(requestComplete, status=status.HTTP_200_OK)

