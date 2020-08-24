from django.urls import path
from .views import Hello

urlpatterns = [
    path('test/', Hello.as_view())
]


