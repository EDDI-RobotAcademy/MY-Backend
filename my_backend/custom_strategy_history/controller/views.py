from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.account import Account
from custom_strategy_history.entity.custom_strategy_history import CustomStrategyHistory
from custom_strategy_history.serializer import CustomStrategyHistorySerializer
from custom_strategy_history.service.custom_strategy_history_service_impl import CustomStrategyHistoryServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
import json


class CustomStrategyHistoryView(viewsets.ViewSet):
    customStrategyHistoryService = CustomStrategyHistoryServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def saveCustomStrategyResult(self, request):
        try:
            data = request.data
            if isinstance(data, str):
                data = json.loads(data)
            userToken = data.get("userToken")
            request_id = data.get("request_id")
            aiResult = data.get("generatedText")
            print(f"userToken: {userToken}, request_id: {request_id} aiResult: {aiResult}")

            self.customStrategyHistoryService.saveStrategyData(request_id, aiResult)

            return Response({'message': '전략 저장 성공'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"에러 발생: {str(e)}")
            return Response({'error': f'전략 저장 실패: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def readCustomStrategyResult(self, request):
        try:
            data = request.data
            if isinstance(data, str):
                data = json.loads(data)
            userToken = data.get("userToken")
            request_id = data.get("request_id")
            print(f"userToken: {userToken}, request_id: {request_id} ")

            try:
                strategy = self.customStrategyHistoryService.readStrategyData(request_id)
                serializer = CustomStrategyHistorySerializer(strategy, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CustomStrategyHistory.DoesNotExist:
                return Response({'error': '전략을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"에러 발생: {e}")
            return Response({'error': f'전략 조회 실패: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)