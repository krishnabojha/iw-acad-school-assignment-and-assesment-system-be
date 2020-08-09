from django.urls import path
from restapi1.views import add_two_number, add_two_number_rest, info_views
from rest_framework.authtoken.views import obtain_auth_token
from restapi1.class_views import InfoClassBasedViews
from .generic_views import GenericsCreateAPIView, InfoModelListAPIView, InfoModelDeleteAPIView, InfoModelUpdateview, InfoModelRetrieveView
from .viewset_views import InfoModelViewset


# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('viewset/', InfoModelViewset)
urlpatterns = [
    # function based views
    path('add/', add_two_number),
    path('v2/add/', add_two_number_rest),
    path('info/', info_views),
    path('info/<int:pk>/',info_views),
    # class based views
    path('class_based/',InfoClassBasedViews.as_view()),
    # rest frame work based generic views
    path('generic_view_create/', GenericsCreateAPIView.as_view()),
    path('generic_view_list/', InfoModelListAPIView.as_view()),
    path('generic_view_delete/<pk>/', InfoModelDeleteAPIView.as_view()),
    path('generic_view_update/<int:pk>/', InfoModelUpdateview.as_view()),
    path('generic_view_retrieve/<int:pk>/', InfoModelRetrieveView.as_view()),
    
    # rest frame work based viewset
    path('viewset/', InfoModelViewset.as_view(actions = {'get': 'list', 'post':'create'})),
    path('login/', obtain_auth_token),
]