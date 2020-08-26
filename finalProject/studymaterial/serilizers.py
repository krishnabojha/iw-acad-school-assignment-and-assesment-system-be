from rest_framework import serializers
from .models import ClassRoom, StudyMaterial
from django.contrib.auth.models  import User
from Authentication.serializer import UserSignUpModelSerializer

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'classname', 'email', 'created_at']
        # read_only = ['id']

class StudyMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ['id', 'file_title', 'video_title', 'files', 'videos', 'created_at', 'updated_at', 'classid']

class StudentClassModelSerializer(serializers.ModelSerializer):
    # classsuser = serializers.PrimaryKeyRelatedField(many=True, queryset=ClassRoom.objects.all())
    classroom_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    class Meta:
        model = ClassRoom
        fields = ['classroom_id', 'user_id']
class StudentClassListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth = 1