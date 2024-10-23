from django.db import models

from account.entity.account import Account


class CustomStrategyHistory(models.Model):
    id = models.AutoField(primary_key=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='custom_strategies'
    )

    strategy_result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Custom Strategy History(ID: {self.id}) -> account: {self.account}, created: {self.created_at}"

    class Meta:
        db_table = 'custom_strategy_history'
        app_label = 'custom_strategy_history'
        ordering = ['-created_at']