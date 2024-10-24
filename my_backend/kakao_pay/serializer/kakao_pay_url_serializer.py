from rest_framework import serializers

class KakaoPayUrlSerializer(serializers.Serializer):
    url = serializers.URLField()
