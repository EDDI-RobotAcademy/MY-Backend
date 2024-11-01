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
            data = request.data
            userToken = data.get("userToken")
            request_id = data.get("request_id")
            aiResult = data.get("generatedText")
            print(f"userToken: {userToken}, request_id: {request_id} aiResult: {aiResult}")

            self.customStrategyHistoryService.saveStrategyData(request_id, aiResult)

            return Response({'message': '전략 저장 성공'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"에러 발생: {str(e)}")
