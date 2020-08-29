from rest_framework import serializers
from .models import AssignmentPDF, ClassRoom, AssignmentSubmit, AssignmentGrades



class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['classname', 'email', 'classuser']

class AssignmentPDFModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentPDF
        fields = ['file_title', 'files', 'created_at', 'updated_at', 'classid']

class AssignmentSubmitSerializer(serializers.ModelSerializer):
    grades = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AssignmentSubmit
        fields = ['assignment_id', 'submitter', 'files', 'grades']

class AssignmentGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentGrades
        fields = ['submitted_asignment', 'score']