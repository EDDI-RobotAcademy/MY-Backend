from rest_framework import viewsets, status
from rest_framework.response import Response

from account.entity.account import Account
from custom_strategy_history.entity.custom_strategy_history import CustomStrategyHistory
from custom_strategy_history.serializer import CustomStrategyHistorySerializer
from custom_strategy_history.service.custom_strategy_history_service_impl import CustomStrategyHistoryServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
import json

from user_analysis.repository.user_analysis_request_repository_impl import UserAnalysisRequestRepositoryImpl


class CustomStrategyHistoryView(viewsets.ViewSet):
    customStrategyHistoryService = CustomStrategyHistoryServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    userAnalysisRequestRepository = UserAnalysisRequestRepositoryImpl.getInstance()

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

            if userToken:
                user_identifier = self.redisService.getValueByKey(userToken)
                print(f"user_identifier: {user_identifier}")

                # 회원/비회원 구분
                if isinstance(user_identifier, int):
                    account_id = user_identifier
                    guest_identifier = None
                else:
                    account_id = None
                    guest_identifier = user_identifier
            else:
                account_id = None
                guest_identifier = None

            # 회원과 비회원에 따라 최신 요청 가져오기
            if account_id is not None:
                # 회원의 최신 요청 조회
                user_analysis_request = self.userAnalysisRequestRepository.findLatestByAccount(account_id)
            else:
                # 비회원의 최신 요청 조회
                user_analysis_request = self.userAnalysisRequestRepository.findLatestByIdentifier(guest_identifier)

            # 요청이 없는 경우 처리
            if not user_analysis_request:
                return Response({'error': '해당 사용자의 요청을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

            # 최신 요청 ID 가져오기
            request_id = user_analysis_request.id
            print(f"userToken: {userToken}, request_id: {request_id}")

            try:
                strategy = self.customStrategyHistoryService.readStrategyData(request_id)
                serializer = CustomStrategyHistorySerializer(strategy, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except CustomStrategyHistory.DoesNotExist:
                return Response({'error': '전략을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"에러 발생: {e}")
            return Response({'error': f'전략 조회 실패: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)