from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()



class UserLoadTestCase(TestCase):
    def setUp(self):
        self.url = reverse('user-list')

    def test_homepage_loads_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class UserCreateAPITest(APITestCase):
    def setUp(self):
        self.url = reverse('user-list')
    def UserCreateTest(self):
        data = {
            'username': 'islamgg',
            'email': 'islam11@gmail.com',
            'password_1': "test123",
            'password_2': "test123",

        }

        response = self.client.post(
            path=self.url,
            data=data
        )

        # status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        expected_data = {
            "username": "islamgg",
            "email": "islam11@gmail.com"
        }

        self.assertEqual(response.data, expected_data)

        # правильно ли записалось
        user = User.objects.get(username="islamgg")
        self.assertEqual(user.username, data["username"])
        self.assertEqual(user.email, data["email"])

# Create your tests here.
