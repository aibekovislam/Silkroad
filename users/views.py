from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
