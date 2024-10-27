from django.db import models

from account.entity.account import Account


class SmartContent(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content_type = models.CharField(max_length=50, null=True)
    nickname = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='smart_content_account')
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'smart_content'
