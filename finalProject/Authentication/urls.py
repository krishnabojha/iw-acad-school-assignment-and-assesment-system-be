from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserListApiView, UserCreateApiView, UserDeleteAPIView, UserUpdateview

urlpatterns = [
    path('create/', UserCreateApiView.as_view()),
    path('list/', UserListApiView.as_view()),
    path('update/<pk>', UserUpdateview.as_view()),
    path('delete/<pk>', UserDeleteAPIView.as_view()),
    path('login/', obtain_auth_token),


]