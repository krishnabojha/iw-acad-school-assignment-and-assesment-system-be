from rest_framework import serializers
from .models import ClassRoom, StudyMaterial

# class ClassroomSerializer(serializers.Serializer):
#     classname = serializers.CharField(max_length = 100)
#     email = serializers.EmailField()
#     created_at = serializers.DateTimeField(auto_now_add = True)

#     def create(self, validated_data):
#         return ClassRoom.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.classname = validated_data['classname']
#         instance.email = validated_data['email']
#         instance.save()
#         return instance

# class StudyMaterialSerializer(serializers.Serializer):
#     files = serializers.FileField(upload_to = 'static/files', blank = True, null = True)
#     videos = serializers.FileField(upload_to = 'static/videos', blank = True, null = True)
#     classid = serializers.ForeignKey(ClassRoom, on_delete = models.CASCADE)
#     created_at = serializers.DateTimeField(auto_now_add = True)
#     updated_at = serializers.DateTimeField(auto_now = True)

#     def create(self, validated_data):
#         return StudyMaterial.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.files = validated_data['files']
#         instance.videos = validated_data['videos']
#         instance.save()
#         return instance

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['id', 'classname', 'email', 'created_at']
        # read_only = ['id']

class StudyMaterialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = ['id', 'files', 'videos', 'created_at', 'updated_at', 'classid']