from rest_framework import serializers
from .models import Response, Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer',)

class ResponseSerializer(serializers.ModelSerializer):

    q_text = serializers.CharField(source='q.question')
    a = AnswerSerializer(read_only=True, many=True)
    s_text = serializers.CharField(source='survey.name')
    free_q_text = serializers.CharField(source='free_q.free_question')


    class Meta:
        model = Response
        fields = ('id', 'q', 'q_text', 'a', 'gender', 'age', 'zip_code', 'home', 'free_q_text', 'free_resp', 'survey', 's_text', 'timestamp', 'front', 'back', )

class QACountSerializer(serializers.Serializer):

    q_id = serializers.IntegerField()
    # q_text = serializers.CharField()
    a_id  = serializers.IntegerField(source='id')
    a_text  = serializers.CharField()
    total = serializers.IntegerField()

class QCountSerializer(serializers.Serializer):

    q = serializers.IntegerField()
    q_text  = serializers.SerializerMethodField()
    total = serializers.IntegerField()

    def get_q_text(self, obj):
        return Question.objects.filter(id=obj['q']).values_list('question', flat=True)[0]