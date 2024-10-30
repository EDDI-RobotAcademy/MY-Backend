from django.db import models

from account.entity.account import Account
from smart_content.entity.models import SmartContent


class LikeCount(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    smart_content = models.ForeignKey(SmartContent, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('account', 'smart_content')

        db_table = 'like_count'
        app_label = 'like_count'
