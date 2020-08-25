from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serilizers import ClassRoomModelSerializer, StudyMaterialModelSerializer
from .serilizers import ClassRoom, StudyMaterial
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
        return StudyMaterial.objects.filter(classid = self.kwargs.get('pk'))

class StudyDeleteAPIView(DestroyAPIView):
    queryset = StudyMaterial.objects.all()

class StudyUpdateview(UpdateAPIView):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialModelSerializer

class StudyRetrieveView(RetrieveAPIView):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialModelSerializer