from django.db import models

from account.entity.account import Account
from free_community.entity.FreeCommunityCategory import FreeCommunityCategory


class FreeCommunity(models.Model):
    free_communityId = models.AutoField(primary_key=True)
    category = models.ForeignKey(FreeCommunityCategory, on_delete=models.CASCADE, related_name='free_communitys')
    categoryFreeCommunityId = models.PositiveIntegerField()
    title = models.CharField(max_length=128, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='free_community_account')
    content = models.TextField()
    contentImage = models.CharField(max_length=100, null=True)
    is_notice = models.BooleanField(default=False)
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'free_community'
        unique_together = ('category', 'categoryFreeCommunityId')

    def save(self, *args, **kwargs):
        if not self.categoryFreeCommunityId:
            max_id = FreeCommunity.objects.filter(category=self.category).aggregate(models.Max('categoryFreeCommunityId'))[
                'categoryFreeCommunityId__max']
            self.categoryFreeCommunityId = (max_id or 0) + 1
        super().save(*args, **kwargs)
