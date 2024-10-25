from django.db import models

from account.entity.account import Account
from user_analysis.entity.user_analysis import UserAnalysis


class UserAnalysisRequest(models.Model):
    id = models.AutoField(primary_key=True)
    user_analysis = models.ForeignKey(UserAnalysis, related_name='user_analysis_requests', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='user_analysis_requests', on_delete=models.CASCADE, null=True,
                                default=None)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'user_analysis_request'
        app_label = 'user_analysis'