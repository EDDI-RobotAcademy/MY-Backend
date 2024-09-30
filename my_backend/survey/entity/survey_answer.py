from django.db import models
from account.entity.account import Account
from survey.entity.survey import Survey
from survey.entity.survey_question import SurveyQuestion
from survey.entity.fixed_five_score_selection import FixedFiveScoreSelection
from survey.entity.fixed_boolean_selection import FixedBooleanSelection
from survey.entity.custom_selection import CustomSelection


class SurveyAnswer(models.Model):
    survey = models.ForeignKey(Survey, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(SurveyQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True) # 서술형 답변
    five_score_selection = models.ForeignKey(FixedFiveScoreSelection, blank=True, null=True, on_delete=models.SET_NULL)
    boolean_selection = models.ForeignKey(FixedBooleanSelection, blank=True, null=True, on_delete=models.SET_NULL)
    custom_selection = models.ForeignKey(CustomSelection, blank=True, null=True, on_delete=models.SET_NULL)
    account = models.ForeignKey(Account, related_name='answers', on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"Answer to {self.question.question_text}"

    class Meta:
        db_table = 'survey_answer'
        app_label = 'survey'