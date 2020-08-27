from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serilizers import (
    ClassRoomModelSerializer,
    StudyMaterialModelSerializer,
    AssignmentModelSerializer,
    AssignmentPDFModelSerializer)
from .serilizers import ClassRoom, StudyMaterial, AssignmentPDF, Assignment
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from rest_framework.response import Response
# from rest_framework.status import (
#     HTTP_201_CREATED,
#     HTTP_400_BAD_REQUEST
# )


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


##### assignmentpdf api view
class AssignmentPDFCreateApiView(CreateAPIView):
    serializer_class = AssignmentPDFModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()


class AssignmentPDFListApiView(ListAPIView):
    serializer_class = AssignmentPDFModelSerializer

    def get_queryset(self):
        print('Id of class(pk) : ', self.kwargs.get('pk'))
        return AssignmentPDF.objects.filter(classid=self.kwargs.get('pk'))


class AssignmentPDFDeleteAPIView(DestroyAPIView):
    queryset = AssignmentPDF.objects.all()


class AssignmentPDFUpdateview(UpdateAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelSerializer


class AssignmentPDFRetrieveView(RetrieveAPIView):
    queryset = AssignmentPDF.objects.all()
    serializer_class = AssignmentPDFModelSerializer


##### assignment api view
class AssignmentCreateApiView(CreateAPIView):
    serializer_class = AssignmentModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()

    # serializer_class = AssignmentModelSerializer
    # queryset = Assignment.objects.all()
    #
    # def create(self, request):
    #     serializer = AssignmentModelSerializer(data=request.data)
    #     if serializer.is_valid():
    #         assignment = serializer.create(request)
    #         if assignment:
    #             return Response(status=HTTP_201_CREATED)
    #     return Response(status=HTTP_400_BAD_REQUEST)


class AssignmentListApiView(ListAPIView):
    serializer_class = AssignmentModelSerializer

    def get_queryset(self):
        print('Id of class(pk) : ', self.kwargs.get('pk'))
        return Assignment.objects.filter(classid=self.kwargs.get('pk'))


class AssignmentDeleteAPIView(DestroyAPIView):
    queryset = Assignment.objects.all()


class AssignmentUpdateview(UpdateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentModelSerializer


class AssignmentRetrieveView(RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentModelSerializer

