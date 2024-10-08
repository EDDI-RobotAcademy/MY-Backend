from django.db import models
from survey.entity.survey_question import SurveyQuestion

class FixedBooleanSelection(models.Model):
    id = models.AutoField(primary_key=True)
    is_true = models.BooleanField()

    def __str__(self):
        return str(self.is_true)

    class Meta:
        db_table = 'fixed_boolean_selection'
        app_label = 'survey'
