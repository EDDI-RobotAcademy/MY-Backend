from django.db import models
from survey.entity.survey_question import SurveyQuestion

class FixedFiveScoreSelection(models.Model):
    id = models.AutoField(primary_key=True)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.question.question_text} - {self.score}"

    class Meta:
        db_table = 'fixed_five_score_selection'
        app_label = 'survey'