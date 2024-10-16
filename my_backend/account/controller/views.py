from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serilaizers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def registerAccount(self, request):
        try:
            loginType = request.data.get('loginType')
            email = request.data.get('email')
            nickname = request.data.get('nickname')

            account = self.accountService.registerAccount(
                loginType=loginType,
                roleType='NORMAL',
                email=email,
                nickname=nickname
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("계정 생성 중 에러 발생:", e)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def checkAccountRoletype(self, request):
        try:
            userToken = request.data.get('userToken')
            print(f"userToken: {userToken}")
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None


            account = self.accountService.findAccountById(accountId)
            print(f"roleType: {account}")

            serializer = AccountSerializer(account)
            print(f"serializer: {serializer}")
            roleType = serializer.data.get('roleType')
            print(f"roleType: {roleType}")

            return Response(roleType, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)