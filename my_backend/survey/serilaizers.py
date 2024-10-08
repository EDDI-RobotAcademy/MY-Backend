from rest_framework import serializers

from account.serilaizers import ProfileSerializer
from survey.entity.survey_answer import SurveyAnswer
class SurveyAnswerSerializer(serializers.ModelSerializer):
    survey_title = serializers.CharField(source='survey.title', read_only=True)
    profile_nickname = serializers.CharField(source='account.profile.nickname', read_only=True)
    question_text = serializers.CharField(source='question.question_text', read_only=True)
    custom_selection_text = serializers.CharField(source='custom_selection.custom_text', read_only=True,
                                                  default=None)

    class Meta:
        model = SurveyAnswer
        fields = ('id', 'survey_title', 'profile_nickname', 'question_text', 'custom_selection_text', 'answer_text',
                  'boolean_selection', 'five_score_selection', 'response_order', 'created_at')

    def to_representation(self, instance):
        # 기본 직렬화 데이터
        data = super(SurveyAnswerSerializer, self).to_representation(instance)

        # None 값을 가진 필드를 제외
        return {k: v for k, v in data.items() if v is not None}
