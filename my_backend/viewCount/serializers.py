from rest_framework import serializers

class ViewCountSerializer(serializers.Serializer):
    community_id = serializers.IntegerField()
    count = serializers.IntegerField()