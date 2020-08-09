from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status

from .models import Info
# from .serializers import InfoSerializer
from .serializers import InfoModelSerializer

class InfoClassBasedViews(APIView):
    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()
        serializer =InfoModelSerializer(instance = qs, many = True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        current_time = timezone.now()
        print('this is current time : ', current_time)
        context = {
            'current_time': current_time
        }
        serialize = InfoModelSerializer(data = request.data, context = context)
        serialize.is_valid(raise_exception = True)
        serialize.save()
        # return Response({'status':'OK', 'data':serialize.data}, status=201)
        return Response({'status':'OK', 'data':serialize.data}, status=status.HTTP_201_CREATED)