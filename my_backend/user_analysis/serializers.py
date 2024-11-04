from rest_framework import serializers

from user_analysis.entity.user_analysis import UserAnalysis
from user_analysis.entity.user_analysis_answer import UserAnalysisAnswer
from user_analysis.entity.user_analysis_custom_selection import UserAnalysisCustomSelection
from user_analysis.entity.user_analysis_fixed_boolean_selection import UserAnalysisFixedBooleanSelection
from user_analysis.entity.user_analysis_fixed_five_score_selection import UserAnalysisFixedFiveScoreSelection
from user_analysis.entity.user_analysis_question import UserAnalysisQuestion
from user_analysis.entity.user_analysis_request import UserAnalysisRequest


class UserAnalysisAnswerSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question_text', read_only=True)
    user_analysis_custom_selection_text = serializers.CharField(source='custom_selection.custom_text', read_only=True,
                                                  default=None)

    class Meta:
        model = UserAnalysisAnswer
        fields = ('id', 'question_text', 'user_analysis_custom_selection_text', 'answer_text',
                  'boolean_selection', 'five_score_selection')

    def to_representation(self, instance):
        # 기본 직렬화 데이터
        data = super(UserAnalysisAnswerSerializer, self).to_representation(instance)

        # None 값을 가진 필드를 제외
        return {k: v for k, v in data.items() if v is not None}

class UserAnalysisQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAnalysisQuestion
        fields = ('id', 'question_text', 'user_analysis_type')

class UserAnalysisFixedFiveScoreSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysisFixedFiveScoreSelection
        fields = ['id', 'score']

class UserAnalysisFixedBooleanSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysisFixedBooleanSelection
        fields = ['id', 'is_true']

class UserAnalysisCustomSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysisCustomSelection
        fields = ('id', 'custom_text', 'question_id')

class UserAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysis
        fields = ['id', 'title', 'description']

class UserAnalysisRequestSerializer(serializers.ModelSerializer):
    user_analysis_title = serializers.CharField(source='user_analysis.title', read_only=True)
    profile_nickname = serializers.SerializerMethodField()

    class Meta:
        model = UserAnalysisRequest
        fields = ['id', 'user_analysis_title', 'profile_nickname', 'created_at']

    def get_profile_nickname(self, obj):
        if obj.account:
            return obj.account.user_profile.nickname  # 회원일 경우 닉네임 반환
        return "Guest"  # 비회원일 경우 기본 값 반환