
from django.urls import path
from .views import AssignmentPDFCreateApiView, AssignmentPDFListApiView, AssignmentPDFUpdateview, AssignmentPDFDeleteAPIView, AssignmentPDFRetrieveView
from .views import AssignmentSubmitCreateApiView, AssignmentSubmissionList
from .views import CreateGrade, GradeList


urlpatterns = [
    path('assignmentpdf_create/', AssignmentPDFCreateApiView.as_view()),
    path('assignmentpdf_list/<pk>', AssignmentPDFListApiView.as_view()),
    path('assignmentpdf_delete/<pk>/', AssignmentPDFDeleteAPIView.as_view()),
    path('assignmentpdf_update/<int:pk>/', AssignmentPDFUpdateview.as_view()),
    path('assignmentpdf_retrieve/<int:pk>/', AssignmentPDFRetrieveView.as_view()),

    path('assignmentsubmit/create/',AssignmentSubmitCreateApiView.as_view()),
    path('assignmentsubmit/list/',AssignmentSubmissionList.as_view()),

    path('grade/create/', CreateGrade.as_view()),
    path('grade/list/', GradeList.as_view()),
]
