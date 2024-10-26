from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from redis_token.service.redis_service_impl import RedisServiceImpl
from user_profile.entity.user_profile import UserProfile
from user_profile.serializers import UserProfileSerializer
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class UserProfileView(viewsets.ViewSet):
    queryset = UserProfile.objects.all()
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

    def getUserProfileByAccountId(self, request):
        try:
            userToken = request.data.get('userToken')
            if userToken:
                accountId = self.redisService.getValueByKey(userToken)
                userProfile = self.userProfileService.getUserProfileByAccountId(accountId)
                if userProfile:
                    serializer = UserProfileSerializer(userProfile)
                    return Response(serializer.data)
                else:
                    return Response({'error': 'User Profile not found'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return None
        except Exception as e:
            print("유저 프로필 조회 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def getUserProfileByNickname(self, request):
        try:
            nickname = request.data.get('nickname')
            userProfile = self.userProfileService.getUserProfileByNickname(nickname)

            if userProfile:
                serializer = UserProfileSerializer(userProfile)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print("닉네임으로 프로필 조회 중 에러 발생:", e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)





