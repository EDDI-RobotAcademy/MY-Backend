from django.db import models


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'survey'
        app_label = 'survey'