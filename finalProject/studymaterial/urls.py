from django.urls import path
from .views import ClassCreateApiView, ClassListApiView, ClassUpdateview, ClassDeleteAPIView, ClassRetrieveView

urlpatterns = [
    path('studymaterial_create/', ClassCreateApiView.as_view()),
    path('studymaterial_list/', ClassListApiView.as_view()),
    path('studymaterial_delete/<pk>/', ClassDeleteAPIView.as_view()),
    path('studymaterial_update/<int:pk>/', ClassUpdateview.as_view()),
    path('studymaterial_retrieve/<int:pk>/', ClassRetrieveView.as_view()),
]