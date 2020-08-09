from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView,RetrieveAPIView

from .serializers import InfoModelSerializer
from .serializers import Info
from .pagination import MypaginationOffset
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class GenericsCreateAPIView(CreateAPIView):
    serializer_class = InfoModelSerializer

    def perform_create(self, serializer):
        serializer.save()
        print('The serializer is saved.')

class InfoModelListAPIView(ListAPIView):
    # queryset = Info.objects.get()
    serializer_class = InfoModelSerializer
    pagination_class = MypaginationOffset
    filter_backends = [SearchFilter, OrderingFilter]
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    search_fields = ['name']
    order_fields = ['name', 'id']
    filterset_fields = ['name']

    def get_queryset(self):
        return Info.objects.all()

class InfoModelDeleteAPIView(DestroyAPIView):
    queryset = Info.objects.all()

class InfoModelUpdateview(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer

class InfoModelRetrieveView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer