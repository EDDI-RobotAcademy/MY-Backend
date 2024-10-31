from django.db import models

from account.entity.account import Account
from user_analysis.entity.user_analysis_request import UserAnalysisRequest


class CustomStrategyHistory(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(UserAnalysisRequest, related_name='custom_strategy', on_delete=models.CASCADE)
    strategy_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Custom Strategy History(ID: {self.id}) -> request: {self.request}, created: {self.created_at}"

    class Meta:
        db_table = 'custom_strategy_history'
        app_label = 'custom_strategy_history'
        ordering = ['-created_at']