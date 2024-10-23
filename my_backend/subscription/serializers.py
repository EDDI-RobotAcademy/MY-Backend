from rest_framework import serializers

from subscription.entity.subscription import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['name']