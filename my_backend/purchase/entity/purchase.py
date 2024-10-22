from django.db import models
from django.utils import timezone

from account.entity.account import Account


class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='purchase')
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"purchase {self.id} by {self.account}"

    class Meta:
        db_table = 'purchase'
        app_label = "purchase"