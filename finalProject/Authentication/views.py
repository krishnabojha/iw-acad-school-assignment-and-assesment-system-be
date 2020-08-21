from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,UpdateAPIView
from .serializer import UserLoginModelSerializer, UserSignUpModelSerializer, UserTokenSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class UserCreateApiView(CreateAPIView):
    serializer_class = UserSignUpModelSerializer

    def perform_create(self, serilizer):
        serilizer.save()

class UserListApiView(ListAPIView):
    serializer_class = UserLoginModelSerializer

    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return User.objects.all()

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()

class UserUpdateview(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginModelSerializer

# show user token
class UserLoginToken(ListAPIView):
    serializer_class = UserTokenSerializer

    def get_queryset(self):
        return Token.objects.all()