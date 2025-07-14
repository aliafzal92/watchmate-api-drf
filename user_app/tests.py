from typing import override
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username" : "testcase",
            "email" : "testcase@gmail.com",
            "password" : "newpass123",
            "password2" : "newpass123"
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class LoginLogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="newpass123")

    
    def test_login(self):
        data = {
            "username" : "example",
            "password" : "newpass123"
        }
        response = self.client.post(reverse("login"), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        # token = 
        pass