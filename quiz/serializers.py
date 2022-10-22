from rest_framework import serializers
from .models import Quizze, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizze
        fields = [
            'ques',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class AddQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'ques','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz','ques','answer',
        ]