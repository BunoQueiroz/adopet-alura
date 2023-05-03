from rest_framework.test import APITestCase
from core.models import APIUser
from rest_framework import status


class APIUserDeleteRequestsTestCase(APITestCase):
    
    def setUp(self) -> None:
        APIUser.objects.create_user('meu-front-end', 'front@gmail.com', 'senhas001', type='f', company_or_user='usuário qualquer')
        self.users_api = APIUser.objects.filter(username='meu-front-end')
        self.user_api = self.users_api.get()
        self.user_api_id = self.user_api.pk

    def test_api_user_delete_status_404(self):
        """Ao tentar deletar um cliente da API deve retornar status 404"""
        response = self.client.delete(f'/api-users/{self.user_api_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_user_not_delete_in_data_base(self):
        """Ao tentar deletar um cliente da API o banco de dados não deve ser apagados"""
        self.client.delete(f'/api-users/{self.user_api_id}/')
        self.assertTrue(self.users_api.exists())
