from django.db import models

from smart_content.entity.models import SmartContent


class SmartText(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.ForeignKey(SmartContent, on_delete=models.CASCADE)
    text = models.TextField()
    sequence_number = models.IntegerField()

    class Meta:
        db_table = 'smart_text'
        ordering = ['sequence_number']
