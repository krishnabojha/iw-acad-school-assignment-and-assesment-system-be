from django.urls import path
from .views import ClassCreateApiView, ClassListApiView, ClassUpdateview, ClassDeleteAPIView, ClassRetrieveView
from .views import StudyCreateApiView, StudyListApiView, StudyUpdateview, StudyDeleteAPIView, StudyRetrieveView
from .views import AssignmentCreateApiView, AssignmentListApiView, AssignmentUpdateview, AssignmentDeleteAPIView, AssignmentRetrieveView
from .views import AssignmentPDFCreateApiView, AssignmentPDFListApiView, AssignmentPDFUpdateview, AssignmentPDFDeleteAPIView, AssignmentPDFRetrieveView
urlpatterns = [
    path('studymaterial_class_create/', ClassCreateApiView.as_view()),
    path('studymaterial_class_list/', ClassListApiView.as_view()),
    path('studymaterial_class_delete/<pk>/', ClassDeleteAPIView.as_view()),
    path('studymaterial_class_update/<int:pk>/', ClassUpdateview.as_view()),
    path('studymaterial_class_retrieve/<int:pk>/', ClassRetrieveView.as_view()),

    #### url for studymaterial
    path('studymaterial_material_create/', StudyCreateApiView.as_view()),
    path('studymaterial_material_list/<pk>', StudyListApiView.as_view()),
    path('studymaterial_material_delete/<pk>/', StudyDeleteAPIView.as_view()),
    path('studymaterial_material_update/<int:pk>/', StudyUpdateview.as_view()),
    path('studymaterial_material_retrieve/<int:pk>/', StudyRetrieveView.as_view()),

    #### url for assignment
    path('assignment_create/', AssignmentCreateApiView.as_view()),
    path('assignment_list/<pk>', AssignmentListApiView.as_view()),
    path('assignment_delete/<pk>/', AssignmentDeleteAPIView.as_view()),
    path('assignment_update/<int:pk>/', AssignmentUpdateview.as_view()),
    path('assignment_retrieve/<int:pk>/', AssignmentRetrieveView.as_view()),

    #### url for assignmentpdf
    path('assignmentpdf_create/', AssignmentPDFCreateApiView.as_view()),
    path('assignmentpdf_list/<pk>', AssignmentPDFListApiView.as_view()),
    path('assignmentpdf_delete/<pk>/', AssignmentPDFDeleteAPIView.as_view()),
    path('assignmentpdf_update/<int:pk>/', AssignmentPDFUpdateview.as_view()),
    path('assignmentpdf_retrieve/<int:pk>/', AssignmentPDFRetrieveView.as_view()),
]