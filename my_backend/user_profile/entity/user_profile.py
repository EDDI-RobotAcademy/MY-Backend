from django.db import models

from account.entity.account import Account

class UserProfile(models.Model):
    nickname = models.CharField(max_length=64, null=False)
    email = models.CharField(max_length=64, unique=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return f"Profile -> email: {self.email}, nickname: {self.nickname}"

    class Meta:
        db_table = 'user_profile'
        app_label = 'user_profile'
