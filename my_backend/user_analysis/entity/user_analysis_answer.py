from django.db import models
from account.entity.account import Account
from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_fixed_boolean_selection import UserAnalysisFixedBooleanSelection
from user_analysis.entity.user_analysis_fixed_five_score_selection import UserAnalysisFixedFiveScoreSelection

from user_analysis.entity.user_analysis_question import UserAnalysisQuestion
from user_analysis.entity.user_analysis_request import UserAnalysisRequest


class UserAnalysisAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    request = models.ForeignKey(UserAnalysisRequest, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(UserAnalysisQuestion, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    five_score_selection = models.ForeignKey(UserAnalysisFixedFiveScoreSelection, blank=True, null=True, on_delete=models.SET_NULL)
    boolean_selection = models.ForeignKey(UserAnalysisFixedBooleanSelection, blank=True, null=True, on_delete=models.SET_NULL)
    custom_selection = models.ForeignKey(UserAnalysisCustomSelection, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Answer to {self.question.question_text}"

    class Meta:
        db_table = 'user_analysis_answer'
        app_label = 'user_analysis'