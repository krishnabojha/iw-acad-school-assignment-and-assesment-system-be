
from django.urls import path
import assignment.views as apiviews

urlpatterns = [
    path('assignmentpdf_create/', apiviews.AssignmentPDFCreateApiView.as_view()),
    path('assignmentpdf_list/<pk>', apiviews.AssignmentPDFListApiView.as_view()),
    path('assignmentpdf_delete/<pk>/', apiviews.AssignmentPDFDeleteAPIView.as_view()),
    path('assignmentpdf_update/<int:pk>/', apiviews.AssignmentPDFUpdateview.as_view()),
    path('assignmentpdf_retrieve/<int:pk>/', apiviews.AssignmentPDFRetrieveView.as_view()),

    path('assignmentsubmit/create/',apiviews.AssignmentSubmitCreateApiView.as_view()),
    path('assignmentsubmit/list/',apiviews.AssignmentSubmissionList.as_view()),
    path('assignmentsubmit/delete/<int:pk>', apiviews.AssignmentSubmissionDelete.as_view()),

    path('grade/create/', apiviews.CreateGrade.as_view()),
    path('grade/delete/<int:pk>', apiviews.GradeDelete.as_view()),
    path('grade/update/<int:pk>', apiviews.GradeUpdate.as_view()),
    path('grade/list/', apiviews.GradeList.as_view()),
]
