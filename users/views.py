from django.shortcuts import render
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import CreateAPIView
# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny
# Подключаем модель User
from .models import User

User = get_user_model()

class UserListAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializers_class = UserSerializer
    queryset = User.objects.all()

class RegistrationsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_object = RegistrationSerializer(data=request.POST)
        if user_object.is_valid:
            password_1 = user_object.validated_data.get("password_1")
            password_2 = user_object.validated_data.get("password_2")
            if password_1 == password_2:
                user = User.save()
                user.username = user_object.validated_data.get("username")
                user.email = user_object.validated_data.get("email")
                return Responce(data=UserSerializer(user).data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={"error": "Пароли не совпадают"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data=user_object.errors, status=status.HTTP_400_BAD_REQUEST)