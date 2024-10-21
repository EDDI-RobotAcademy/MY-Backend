from django.db import models

from account.entity.account import Account
from board.entity.boardcategory import BoardCategory


class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    category = models.ForeignKey(BoardCategory, on_delete=models.CASCADE, related_name='boards')
    categoryBoardId = models.PositiveIntegerField()
    title = models.CharField(max_length=128, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='board_account')
    content = models.TextField()
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        unique_together = ('category', 'categoryBoardId')

    def save(self, *args, **kwargs):
        if not self.categoryBoardId:
            max_id = Board.objects.filter(category=self.category).aggregate(models.Max('categoryBoardId'))[
                'categoryBoardId__max']
            self.categoryBoardId = (max_id or 0) + 1
        super().save(*args, **kwargs)
