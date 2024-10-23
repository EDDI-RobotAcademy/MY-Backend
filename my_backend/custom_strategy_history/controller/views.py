from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.account import Account
from custom_strategy_history.entity.custom_strategy_history import CustomStrategyHistory
from custom_strategy_history.service.custom_strategy_history_service_impl import CustomStrategyHistoryServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
import json


class CustomStrategyHistoryView(viewsets.ViewSet):
    customStrategyHistoryService = CustomStrategyHistoryServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def saveCustomStrategyResult(self, request):
        try:
            request_data = json.loads(request.data)
            userToken = request_data.get("userToken")
            aiResult = request_data.get("aiResult")
            print(f"userToken: {userToken}, aiResult: {aiResult}")

            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
                print(f"accountId: {accountId}")
            else:
                accountId = None

            if accountId:
                self.customStrategyHistoryService.saveStrategyData(accountId, aiResult)
            else:
                print(f"userToken 부합하는 accountId가 존재하지 않습니다.")

            return Response({'message': '전략 저장 성공'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"에러 발생: {str(e)}")
