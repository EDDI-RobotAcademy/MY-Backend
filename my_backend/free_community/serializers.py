from rest_framework import serializers

from free_community.entity.FreeCommunityCategory import FreeCommunityCategory
from free_community.entity.models import FreeCommunity



class FreeCommunitySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    profile_nickname = serializers.CharField(source='account.user_profile.nickname')

    class Meta:
        model = FreeCommunity
        fields = ['free_communityId', 'category_name', 'categoryFreeCommunityId', 'profile_nickname', 'title', 'content', 'contentImage', 'is_notice', 'regDate', 'updDate']
        read_only_fields = ['free_communityId', 'regDate', 'updDate', 'categoryFreeCommunityId']

    def validate_category_id(self, value):
        try:
            FreeCommunityCategory.objects.get(pk=value)
        except FreeCommunityCategory.DoesNotExist:
            raise serializers.ValidationError(f"Category with id {value} does not exist.")
        return value

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = FreeCommunityCategory.objects.get(pk=category_id)
        free_community = FreeCommunity.objects.create(category=category, **validated_data)
        return free_community


class FreeCommunityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeCommunityCategory
        fields = ['categoryId', 'name']
