from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serilizers import (ClassRoomModelSerializer, StudyMaterialModelSerializer, 
                        StudentClassModelSerializer, StudentClassListModelSerializer, 
                        UserInfoModelSerializer)
from .serilizers import ClassRoom, StudyMaterial, UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ClassCreateApiView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()

class ClassListApiView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return ClassRoom.objects.all()

class ClassDeleteAPIView(DestroyAPIView):
    queryset = ClassRoom.objects.all()

class ClassUpdateview(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer

class ClassRetrieveView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
##### study material api view
class StudyCreateApiView(CreateAPIView):
    serializer_class = StudyMaterialModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()

class StudyListApiView(ListAPIView):
    serializer_class = StudyMaterialModelSerializer
    def get_queryset(self):
        print('Id of class(pk) : ', self.kwargs.get('pk'))
        print('this is many to many ', ClassRoom.objects.filter(classuser = 18))
        return StudyMaterial.objects.filter(classid = self.kwargs.get('pk'))

class StudyDeleteAPIView(DestroyAPIView):
    queryset = StudyMaterial.objects.all()

class StudyUpdateview(UpdateAPIView):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialModelSerializer

class StudyRetrieveView(RetrieveAPIView):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialModelSerializer

######## Student Class many to many relation(display list of the class of the user)
class StudentUserCreateView(CreateAPIView):
    serializer_class = StudentClassModelSerializer
    def perform_create(self, request):
        print('this is classroom id',request.data['classroom_id'])
        print('this is user id', request.data['user_id'])
        ClassRoom.objects.get(id = request.data['classroom_id']).classuser.add(request.data['user_id'])
    #     # serializer.save()
    
class StudentUserListView(ListAPIView):
    serializer_class = StudentClassListModelSerializer
    def get_queryset(self):
        print('Id of class(pk) : ', self.kwargs.get('pk'))
        # print('this is many to many ', ClassRoom.objects.filter(classuser = self.kwargs.get('pk'))[1].classname)
        return ClassRoom.objects.filter(classuser = self.kwargs.get('pk'))

# user profile api
class UserInfoCreateView(CreateAPIView):
    serializer_class = UserInfoModelSerializer

    def perform_create(self, serializer):
        serializer.save()
class UserInfoListView(ListAPIView):
    serializer_class = UserInfoModelSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(userid= self.kwargs.get('pk'))

class UserInfoUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserInfoModelSerializer