from django.db import models

from smart_content.entity.models import SmartContent


class SmartImage(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.ForeignKey(SmartContent, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    sequence_number = models.IntegerField()

    class Meta:
        db_table = 'smart_image'
        ordering = ['sequence_number']
