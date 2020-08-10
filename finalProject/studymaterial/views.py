from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serilizers import ClassRoomModelSerializer
from .serilizers import ClassRoom

class ClassCreateApiView(CreateAPIView):
    serializer_class = ClassRoomModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()

class ClassListApiView(ListAPIView):
    serializer_class = ClassRoomModelSerializer
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