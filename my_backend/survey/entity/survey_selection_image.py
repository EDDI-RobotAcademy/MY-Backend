from django.db import models

from survey.entity.survey_selection import SurveySelection


class SurveySelectionImage(models.Model):
    id = models.AutoField(primary_key=True)
    survey_selection_id = models.ForeignKey(SurveySelection, on_delete=models.CASCADE)
    selection_image = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'survey_selection_image'
        app_label = 'survey'