from rest_framework import viewsets, status
from rest_framework.response import Response

from purchase.service.purchase_service_impl import PurchaseServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl
from subscription.serializers import SubscriptionSerializer


class PurchaseView(viewsets.ViewSet):
    purchaseService = PurchaseServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createPurchase(self, request):
        try:
            data = request.data
            print('data: ', data)

            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            purchaseSubscription = data.get('purchaseSubscription')

            purchaseId = self.purchaseService.createPurchase(accountId, purchaseSubscription)
            return Response(purchaseId, status=status.HTTP_200_OK)

        except Exception as e:
            print('구독 과정 중 문제 발생: ', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkIsSubscribe(self, request):
        try:
            data = request.data
            userToken = data.get('userToken')
            accountId = self.redisService.getValueByKey(userToken)

            if not accountId:
                raise ValueError('Invalid userToken')

            recentPurchasedSubscription = self.purchaseService.getRecentPurchaseSubscription(accountId)
            if recentPurchasedSubscription is None:
                return Response({'message': 'No recent subscription or more than one month since last purchase'},
                                status=status.HTTP_200_OK)
            serializer = SubscriptionSerializer(recentPurchasedSubscription.subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print('구독권 확인 중 문제 발생: ', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



