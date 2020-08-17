from rest_framework import serializers
from .models import ClassRoom, StudyMaterial

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'classname', 'email', 'created_at']
        # read_only = ['id']

class StudyMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ['id', 'file_title', 'video_title', 'files', 'videos', 'created_at', 'updated_at', 'classid']