from rest_framework import viewsets, status
from rest_framework.response import Response

from growth_blog.entity.follow_list import growth_list
from redis_token.service.redis_service_impl import RedisServiceImpl
from user_profile.service.user_profile_service_impl import UserProfileServiceImpl


class GrowthBlogView(viewsets.ViewSet):
    userProfileService = UserProfileServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def registerFollowingAndFollowers(self, request):
        try:
            FollowerNickname = request.data.get('FollowerNickname')
            userToken = request.data.get('userToken')

            if not FollowerNickname:
                return Response({'error': 'Nickname이 필요합니다.'}, status=status.HTTP_400_BAD_REQUEST)

            # 팔로우 대상 유저 정보 가져오기
            userProfile = self.userProfileService.getUserProfileByNickname(FollowerNickname)
            if not userProfile:
                return Response({'error': '유효하지 않은 nickname입니다.'}, status=status.HTTP_400_BAD_REQUEST)

            # 현재 로그인한 유저의 account_id 가져오기
            myAccountId = self.redisService.getValueByKey(userToken)
            if not myAccountId:
                return Response({'error': '유효하지 않은 토큰입니다.'}, status=status.HTTP_401_UNAUTHORIZED)

            userAccountId = userProfile.account.id

            try:
                # 팔로우 대상 유저의 growth_blog 가져오기 또는 생성
                target_growth_blog, target_created = growth_list.objects.get_or_create(
                    account__id=userAccountId,
                    defaults={
                        'following': '',
                        'followers': '',
                        'account_id': userAccountId
                    }
                )

                # 내 growth_blog 가져오기 또는 생성
                my_growth_blog, my_created = growth_list.objects.get_or_create(
                    account__id=myAccountId,
                    defaults={
                        'following': '',
                        'followers': '',
                        'account_id': myAccountId
                    }
                )

                # 팔로우 관계 업데이트
                # 대상 유저의 followers에 내 ID 추가
                followers_list = target_growth_blog.followers.split(',') if target_growth_blog.followers else []
                if str(myAccountId) not in followers_list:
                    followers_list.append(str(myAccountId))
                    target_growth_blog.followers = ','.join(filter(None, followers_list))

                # 내 following에 대상 유저 ID 추가
                following_list = my_growth_blog.following.split(',') if my_growth_blog.following else []
                if str(userAccountId) not in following_list:
                    following_list.append(str(userAccountId))
                    my_growth_blog.following = ','.join(filter(None, following_list))

                # 변경사항 저장
                target_growth_blog.save()
                my_growth_blog.save()

                return Response({
                    'message': '팔로우 관계가 성공적으로 등록되었습니다.',
                    'following': my_growth_blog.following,
                    'followers': target_growth_blog.followers
                }, status=status.HTTP_200_OK)

            except growth_list.DoesNotExist:
                return Response({'error': '사용자 정보를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print('팔로우 관계 등록 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def followingByNickname(self, request):
        print("followingByNickname 접근")
        try:
            nickname = request.data.get('nickname')
            if nickname:
                userProfile = self.userProfileService.getUserProfileByNickname(nickname)
            else:
                userProfile = None

            if userProfile:
                account_id = userProfile.account.id
                print("어카운트 id 입니다", account_id)

                growth_blog = growth_list.objects.get(account__id=account_id)
                following = growth_blog.following

                return Response({'following': following}, status=status.HTTP_200_OK)
            else:
                return Response({'error': '유효하지 않은 nickname입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        except growth_list.DoesNotExist:
            return Response({'error': '팔로잉 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print('nickname으로 smart content list 출력 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
