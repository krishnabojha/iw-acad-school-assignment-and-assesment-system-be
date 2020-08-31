from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,UpdateAPIView
from .serializer import (UserLoginModelSerializer, UserSignUpModelSerializer,
                        UserTokenSerializer, ResetUserpasswordModelSerializer, OTPModelSerializer)
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail

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

### password reset
class UserPasswordReset(CreateAPIView):
    serializer_class = ResetUserpasswordModelSerializer
    def perform_create(self, request):
        print('password this: ',request.data['newpassword'])
        changeobject = User.objects.get(id = self.kwargs.get('pk'))
        changeobject.set_password(request.data['newpassword'])
        changeobject.save()

class SendMail(CreateAPIView):
    serializer_class = OTPModelSerializer
    def perform_create(self, request):
        print('this is send mail', request.data['otpcode'])
        send_mail(subject='Your OTP code', message= 'Enter this otp code to reset  password :\n'+str(request.data['otpcode']), from_email= 'admin@admin', recipient_list= [request.data['email'], ])