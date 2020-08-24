
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import permissions

from .models import User
from .serializers import UserSerializer, RegisterSerializer

class RegisterAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.pop('password')
        validated_data = serializer.validated_data
        user = User.objects.create(**validated_data)
        user.save()
        return Response(validated_data)

class UserAPI(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        self.request.user