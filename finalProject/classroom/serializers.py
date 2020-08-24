from rest_framework import serializers
from .models import Subject, Assignment, Question, Answer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject


class AssignmentSerializer(seriaizers.ModelSerializer):
    class Meta:
        model= Assignment
        fields = ['owner', 'name','subject']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['assignments', 'text']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'text', 'is_correct']
