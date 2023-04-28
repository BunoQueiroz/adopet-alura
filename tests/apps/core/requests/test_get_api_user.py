from rest_framework.test import APITestCase
from rest_framework import status
from core.models import APIUser
from django.urls import reverse


class APIUserGetRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.api_user = APIUser.objects.create_user('api-user', 'emailapi@gmail.com', 'senhas001', company_or_user='usuário qualquer', type='m',)
        self.api_user_id = APIUser.objects.get(username='api-user').pk
        self.url = reverse('api-users')

    def test_api_user_get_all_api_users(self):
        """Não deve ser possível ver todos os clientes que utilizam a API"""
        response = self.client.get(f'{self.url}')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_api_user_get_user_by_id(self):
        """Não deve ser possível qualquer clientes da API através de seu ID"""
        response = self.client.get(f'{self.url}{self.api_user_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
