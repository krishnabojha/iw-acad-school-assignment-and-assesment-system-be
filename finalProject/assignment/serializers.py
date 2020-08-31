from rest_framework import serializers
from .models import AssignmentPDF, ClassRoom, AssignmentSubmit, AssignmentGrades
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['classname', 'email', 'classuser']
        depth = 1



class AssignmentSubmitReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmit
        fields = ['assignment_id', 'submitter', 'files', 'id']
        depth = 1

class AssignmentSubmitWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmit
        fields = ['assignment_id', 'submitter', 'files', 'id']


class AssignmentPDFModelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['file_title', 'files', 'created_at', 'updated_at', 'classid']
        depth =1

class AssignmentPDFModelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['file_title', 'files', 'created_at', 'updated_at', 'classid']


class AssignmentGradesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrades
        fields = ['submitted_asignment', 'score']
        depth = 1

class AssignmentGradesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrades
        fields = ['submitted_asignment', 'score']