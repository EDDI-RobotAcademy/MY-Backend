from rest_framework import serializers
from smart_content.entity.models import SmartContent
from smart_content.entity.smart_image import SmartImage
from smart_content.entity.smart_text import SmartText


class SmartContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartContent
        fields = ['id', 'title', 'content_type', 'account', 'regDate', 'updDate']
        read_only_fields = ['regDate', 'updDate']

class SmartTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartText
        fields = ['id', 'content', 'text', 'sequence_number']

class SmartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartImage
        fields = ['id', 'content', 'image_url', 'sequence_number']
