
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import (
    AssignmentPDFModelSerializer,
    AssignmentSubmitSerializer,
    AssignmentGradesSerializer)
from .models import AssignmentPDF, AssignmentSubmit, AssignmentGrades
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class AssignmentPDFCreateApiView(CreateAPIView):
    serializer_class = AssignmentPDFModelSerializer

    def perform_create(self, serializer):
        serializer.save()


class AssignmentPDFListApiView(ListAPIView):
    serializer_class = AssignmentPDFModelSerializer

    def get_queryset(self):
        return AssignmentPDF.objects.filter(classid=self.kwargs.get('pk'))


class AssignmentPDFDeleteAPIView(DestroyAPIView):
    queryset = AssignmentPDF.objects.all()


class AssignmentPDFUpdateview(UpdateAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelSerializer


class AssignmentPDFRetrieveView(RetrieveAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelSerializer

#assignment submission
class AssignmentSubmitCreateApiView(CreateAPIView):
    serializer_class = AssignmentSubmitSerializer

    def perform_create(self, serializer):
        serializer.save()

class AssignmentSubmissionList(ListAPIView):
    serializer_class = AssignmentSubmitSerializer

    def get_queryset(self):
        return AssignmentSubmit.objects.all()

class AssignmentSubmissionDelete(DestroyAPIView):
    queryset = AssignmentSubmit.objects.all()

class AssignmentSubmissionUpdate(UpdateAPIView):
    queryset = AssignmentSubmit.objects.all()
    serializer_class = AssignmentSubmitSerializer

class AssignmentSubmitRetrieve(RetrieveAPIView):
    queryset = AssignmentSubmit.objects.all()
    serializer_class = AssignmentSubmit


# grades
class CreateGrade(CreateAPIView):
    serializer_class = AssignmentGradesSerializer

    def perform_create(self, serializer):
        serializer.save()

class GradeList(ListAPIView):
    serializer_class = AssignmentGradesSerializer

    def get_queryset(self):
        return AssignmentGrades.objects.all()