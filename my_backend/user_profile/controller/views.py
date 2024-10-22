from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from redis_token.service.redis_service_impl import RedisServiceImpl
from user_profile.serializers import UserProfileSerializer
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class UserProfileView(viewsets.ViewSet):
    userProfileService = UserProfileServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def checkEmailDuplication(self, request):
        print("checkEmailDuplication()")

        try:
            email = request.data.get('email')
            isDuplicate = self.userProfileService.checkEmailDuplication(email)

            return Response({'isDuplicate': isDuplicate, 'message': 'Email이 이미 존재' \
                             if isDuplicate else 'Email 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("이메일 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkNicknameDuplication(self, request):
        print("checkNicknameDuplication()")

        try:
            nickname = request.data.get('newNickname')
            print(f"nickname: {nickname}")
            isDuplicate = self.userProfileService.checkNicknameDuplication(nickname)

            return Response({'isDuplicate': isDuplicate, 'message': 'Nickname이 이미 존재' \
                             if isDuplicate else 'Nickname 사용 가능'}, status=status.HTTP_200_OK)
        except Exception as e:
            print("닉네임 중복 체크 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def changeNickname(self, request):
        try:
            userToken = request.data.get('userToken')
            newNickname = request.data.get('newNickname')

            if not userToken or not newNickname:
                return Response({'error': 'userToken과 newNickname은 필수입니다.'}, status=status.HTTP_400_BAD_REQUEST)

            accountId = self.redisService.getValueByKey(userToken)

            isDuplicate = self.userProfileService.checkNicknameDuplication(newNickname)

            if isDuplicate:
                return Response({'error': '중복된 닉네임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                updatedProfile = self.userProfileService.changeNickname(accountId, newNickname)

                return Response({
                    'nickname': updatedProfile.nickname, 'message': '닉네임 변경 성공'
                }, status=status.HTTP_200_OK)


        except Exception as e:
            print("닉네임 변경 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)







