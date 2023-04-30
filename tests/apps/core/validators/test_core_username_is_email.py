from rest_framework.test import APITestCase
from core.models import APIUser
from django.urls import reverse


class APIUserEmailIsUsernameTestCase(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'email': 'email@qualquer.com',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
            'type': 'm',
            'company_or_user': 'fabrica local',
        }
        self.url = reverse('api-users')

    def test_api_user_username_is_email(self):
        """Os usernames dos usuários externos devem ser igual aos seus respectivos emails"""
        self.client.post(self.url, self.data)
        obj = APIUser.objects.get(email=self.data['email'])
        self.assertEqual(obj.username, obj.email)
