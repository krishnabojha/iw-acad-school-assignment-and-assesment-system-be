from django.urls import path
from .views import RegisterAPI, UserAPI
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('register/',RegisterAPI.as_view()),
    path('user/',UserAPI.as_view()),
    path('login/',obtain_auth_token)
]