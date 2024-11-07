from django.db import models
class FreeCommunityCategory(models.Model):
    categoryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'free_community_category'