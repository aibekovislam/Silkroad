from django.test import TestCase
from django.urls import reverse




class UserLoadTestCase(TestCase):
    def setUp(self):
        self.url = reverse('user-list')

    def test_homepage_loads_success(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


# Create your tests here.
