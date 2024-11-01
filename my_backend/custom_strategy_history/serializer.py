from rest_framework import serializers

from custom_strategy_history.entity.custom_strategy_history import CustomStrategyHistory


class CustomStrategyHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomStrategyHistory
        fields = ["strategy_result"]
