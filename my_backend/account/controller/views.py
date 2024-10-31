from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serilaizers import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl

import random

from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class AccountView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    userProfileService = UserProfileServiceImpl.getInstance()

    def registerAccount(self, request):
        try:
            loginType = request.data.get('loginType')
            email = request.data.get('email')
            name = request.data.get('name')

            while True:
                random_number = random.randint(1000000000, 9999999999)
                nickname = f"guest{random_number}"

                isDuplicate = self.userProfileService.checkNicknameDuplication(nickname)

                if not isDuplicate:
                    break

            account = self.accountService.registerAccount(
                loginType=loginType,
                roleType='NORMAL',
                email=email,
                name=name,
                nickname=nickname,
                membership='베이직',
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
            serializer = AccountSerializer(account)
            roleType = serializer.data.get('roleType')
            print(f"roleType: {roleType}")

            return Response(roleType, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)

    def checkAccountLoginType(self, request):
        try:
            userToken = request.data.get('userToken')
            print(f"userToken: {userToken}")
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
            else:
                accountId = None

            account = self.accountService.findAccountById(accountId)
            serializer = AccountSerializer(account)
            loginType = serializer.data.get('loginType')
            print(f"loginType: {loginType}")

            return Response(loginType, status.HTTP_200_OK)

        except Exception as e:
            return Response(False, status.HTTP_400_BAD_REQUEST)