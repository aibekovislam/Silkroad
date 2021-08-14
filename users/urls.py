from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListAPIView.as_view(), name="user-list"),
    path('<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('registrantions', RegistrAPIView.as_view(), name="registr")
]
