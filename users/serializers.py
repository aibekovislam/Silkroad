from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class RegistrationSerializerAPIView(serializers.ModelSerializer):
    password_1 = serializers.CharField(max_length=255)
    password_2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2', 'first_name', 'last_name']