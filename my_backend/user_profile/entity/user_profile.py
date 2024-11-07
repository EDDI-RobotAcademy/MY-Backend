from django.db import models

from account.entity.account import Account

class UserProfile(models.Model):
    name = models.CharField(max_length=64, null=False)
    nickname = models.CharField(max_length=64, null=False, unique=True)
    email = models.CharField(max_length=64, unique=True)
    membership = models.CharField(max_length=64, null=False)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return f"Profile -> email: {self.email}, name: {self.name}, nickname: {self.nickname}, membership: {self.membership}, account: {self.account}"

    class Meta:
        db_table = 'user_profile'
        app_label = 'user_profile'
