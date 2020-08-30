from rest_framework import serializers
from .models import UserProfile, ClassRoom, StudyMaterial
from django.contrib.auth.models  import User
from Authentication.serializer import UserSignUpModelSerializer

# class room serializer
class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'classname', 'email', 'created_at']

# studymaterial serializer
class StudyMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ['id', 'file_title', 'video_title', 'files', 'videos', 'created_at', 'updated_at', 'classid']

# Student and user relation and join class serializer
class StudentClassModelSerializer(serializers.ModelSerializer):
    classroom_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    class Meta:
        model = ClassRoom
        fields = ['classroom_id', 'user_id']

# listing user and it's respective class
class StudentClassListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

# userprofile show serializer
class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','profileImg', 'address', 'bio', 'userid']
        