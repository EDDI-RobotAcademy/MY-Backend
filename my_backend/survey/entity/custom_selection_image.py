from django.db import models

from survey.entity.custom_selection import CustomSelection


class CustomSelectionImage(models.Model):
    id = models.AutoField(primary_key=True)
    survey_selection_id = models.ForeignKey(CustomSelection, on_delete=models.CASCADE)
    selection_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'custom_selection_image'
        app_label = 'survey'