from rest_framework.viewsets import ModelViewSet
from .serializers import InfoModelSerializer
from .models import Info
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .permissions import IsStaffUser


class InfoModelViewset(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()
    authentication_classes =  [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
    # permission_classes = [IsStaffUser,]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action =='destroy':
            permissions = [IsStaffUser]

        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


    