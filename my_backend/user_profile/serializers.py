from rest_framework import serializers

from account.entity.account import Account
from user_profile.entity.user_profile import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'name', 'nickname', 'membership','account']
