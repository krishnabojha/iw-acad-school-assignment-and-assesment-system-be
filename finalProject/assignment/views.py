
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import (
    AssignmentPDFModelReadSerializer,
    AssignmentPDFModelWriteSerializer,
    AssignmentSubmitReadSerializer,
    AssignmentSubmitWriteSerializer,
    AssignmentGradesReadSerializer,
    AssignmentGradesWriteSerializer,)
from .models import AssignmentPDF, AssignmentSubmit, AssignmentGrades
from studymaterial.models import ClassRoom
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class AssignmentPDFCreateApiView(CreateAPIView):
    serializer_class = AssignmentPDFModelWriteSerializer

    def perform_create(self, serializer):
        serializer.save()


class AssignmentPDFListApiView(ListAPIView):
    serializer_class = AssignmentPDFModelReadSerializer

    def get_queryset(self):
        print('assignment filter', AssignmentPDF.objects.filter(classid= ClassRoom.objects.get(id = 5)))
        return  AssignmentPDF.objects.filter(classid= ClassRoom.objects.get(id = self.kwargs.get('pk')))


class AssignmentPDFDeleteAPIView(DestroyAPIView):
    queryset = AssignmentPDF.objects.all()


class AssignmentPDFUpdateview(UpdateAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelWriteSerializer


class AssignmentPDFRetrieveView(RetrieveAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelReadSerializer

#assignment submission
class AssignmentSubmitCreateApiView(CreateAPIView):
    serializer_class = AssignmentSubmitWriteSerializer

    def perform_create(self, serializer):
        serializer.save()

class AssignmentSubmissionList(ListAPIView):
    serializer_class = AssignmentSubmitReadSerializer
    queryset = AssignmentSubmit.objects.all()

class AssignmentSubmissionDelete(DestroyAPIView):
    queryset = AssignmentSubmit.objects.all()

class AssignmentSubmissionUpdate(UpdateAPIView):
    queryset = AssignmentSubmit.objects.all()
    serializer_class = AssignmentSubmitWriteSerializer

class AssignmentSubmitRetrieve(RetrieveAPIView):
    queryset = AssignmentSubmit.objects.all()
    serializer_class = AssignmentSubmitReadSerializer


# grades
class CreateGrade(CreateAPIView):
    serializer_class = AssignmentGradesWriteSerializer

    def perform_create(self, serializer):
        serializer.save()

class GradeList(ListAPIView):
    serializer_class = AssignmentGradesReadSerializer
    queryset = AssignmentGrades.objects.all()

 
class GradeUpdate(UpdateAPIView):
    queryset = AssignmentGrades.objects.all()
    serializer_class = AssignmentGradesWriteSerializer

class GradeDelete(DestroyAPIView):
    queryset = AssignmentGrades.objects.all()
