from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class Hello(APIView): 
    authentication_classes = [TokenAuthentication,] 
    permission_classes = [IsAuthenticated,] 

    def get(self,request):
        content = {'message':'Hello World'}
        return Response(content)