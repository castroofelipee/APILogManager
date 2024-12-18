from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class UserViewTest(APITestCase):
    def test_create_user_view(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpassword",
        }

        response = self.client.post("/api/users/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(username="newuser")
        self.assertEqual(user.email, "newuser@example.com")

    def test_get_users_view(self):
        user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpassword"
        )

        self.client.login(username="admin", password="adminpassword")
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
