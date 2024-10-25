from django.db import models

from account.entity.account import Account
from free_community.entity.models import FreeCommunity


class FreeCommunityComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    free_community = models.ForeignKey(FreeCommunity, on_delete=models.CASCADE, related_name='free_community_comments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='free_community_comment_account')
    content = models.TextField()
    nickname = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.account} on {self.board.title}'

    class Meta:
        db_table = 'free_community_comment'