from my_backend import settings
import redis
import json
from redis_token.service.redis_service import RedisService
class RedisServiceImpl(RedisService):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.redis_client = redis.StrictRedis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD,
                decode_responses=True
            )
        return cls.__instance
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def storeAccessToken(self, userToken, user_data):
        try:
            self.redis_client.set(userToken, json.dumps(user_data))
        except Exception as e:
            print('Error storing access token in Redis:', e)
            raise e

    def getValueByKey(self, key):
        try:
            data = self.redis_client.get(key)
            if data:
                # 가져온 데이터가 JSON 형식인지 확인
                if isinstance(data, str) and (data.startswith('{') and data.endswith('}')):
                    try:
                        user_data = json.loads(data)  # JSON 형식으로 파싱
                        print("user_data: ", user_data)
                        user_type = user_data["user_type"]
                        if user_type == "member":
                            return user_data['account_id']  # 회원의 경우 account_id 반환
                        elif user_type == "guest":
                            return user_data['identifier']  # 비회원의 경우 identifier(IP) 반환
                    except json.JSONDecodeError:
                        print("JSON 디코딩 에러 발생")
                # JSON 형식이 아닌 경우 (예: 정수) 그대로 반환
                return data
            return None
        except Exception as e:
            print("redis_token key로 value 찾는 중 에러 발생:", e)
            raise e

    def deleteKey(self, key):
        try:
            result = self.redis_client.delete(key)
            if result == 1:
                print(f"유저 토큰 삭제 성공: {key}")
                return True
            return False
        except Exception as e:
            print("redis key 삭제 중 에러 발생:", e)
            raise e

    def getUserIdentifier(self, userToken):
        try:
            user_data = self.getValueByKey(userToken)
            if isinstance(user_data, dict):
                user_type = user_data.get('user_type')
                if user_type == 'member':
                    return user_data.get('account_id')
                elif user_type == 'guest':
                    return user_data.get('identifier')
            else:
                print("Error: user_data가 dict 형식이 아님. user_data:", user_data)

            return None
        except Exception as e:
            print("Error retrieving user identifier:", e)
            return None