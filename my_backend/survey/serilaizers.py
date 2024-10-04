from rest_framework import serializers

from survey.entity.survey_answer import SurveyAnswer
class SurveyAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyAnswer
        fields = '__all__'
