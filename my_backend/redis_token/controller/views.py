import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from redis_token.service.redis_service_impl import RedisServiceImpl
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class RedisTokenView(viewsets.ViewSet):
    userProfileService = UserProfileServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def createMemberToken(self, request):
        try:
            data = request.data
            email = data.get('email')
            guest_token = data.get('guestToken')  # 기존 게스트 토큰

            # 이메일이 없으면 오류 반환 (회원용 토큰 발행에는 이메일이 필수)
            if not email:
                return Response({'error': 'Email is required for member token generation'},
                                status=status.HTTP_400_BAD_REQUEST)

            # DB에서 account_id 조회
            account = self.userProfileService.findAccountByEmail(email)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            # 기존 게스트 토큰 삭제
            if guest_token:
                self.redisService.deleteKey(guest_token)

            # 새로운 회원용 유저 토큰 생성
            userToken = str(uuid.uuid4())

            # Redis에 회원 정보 저장
            member_data = {'account_id': account.id, 'user_type': 'member'}
            self.redisService.storeAccessToken(userToken, member_data)

            # 회원용 유저 토큰 반환
            return Response({'userToken': userToken}, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error creating member token:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)
            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print('레디스 토큰 해제 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def createGuestToken(self, request):
        try:
            # 게스트용 유저 토큰 생성
            userToken = f"guest-{uuid.uuid4()}"
            user_ip = request.META.get('REMOTE_ADDR')  # 요청한 클라이언트의 IP 주소를 가져옴

            print("user_ip: ", user_ip)

            # Redis에 게스트 정보 저장
            guest_data = {'identifier': user_ip, 'user_type': 'guest'}
            self.redisService.storeAccessToken(userToken, guest_data)

            return Response({'userToken': userToken}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error creating guest token:', e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)