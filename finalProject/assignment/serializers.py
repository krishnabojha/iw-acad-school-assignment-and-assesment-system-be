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
        fields = ['id','assignment_id', 'submitter', 'files']
        depth = 1

class AssignmentSubmitWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmit
        fields = ['id','assignment_id', 'submitter', 'files']


class AssignmentPDFModelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['id','file_title', 'files', 'created_at', 'updated_at', 'classid','due_date']
        depth =1

class AssignmentPDFModelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['file_title', 'files', 'created_at', 'updated_at', 'classid', 'due_date']


class AssignmentGradesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrades
        fields = ['submitted_asignment', 'score']
        depth = 1

class AssignmentGradesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrades
        fields = ['submitted_asignment', 'score']