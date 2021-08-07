from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListAPIView.as_view(), name="user-list"),
    path('registr', RegistrationsAPIView.as_view(), name='Registrations')
]
