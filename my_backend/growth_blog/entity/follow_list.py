from django.db import models

from account.entity.account import Account

class growth_list(models.Model):
    following = models.CharField(max_length=64, null=False)
    followers = models.CharField(max_length=64, null=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='follow_list')

    def __str__(self):
        return f"following: {self.following}, followers: {self.followers}"

    class Meta:
        db_table = 'follow_list'
        app_label = 'growth_blog'
