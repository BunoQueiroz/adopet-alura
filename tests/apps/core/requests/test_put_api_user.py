from rest_framework.test import APITestCase
from core.models import APIUser
from rest_framework import status


class APIUserPutRequestsTestCase(APITestCase):
    
    def setUp(self) -> None:
        APIUser.objects.create_user('meu-front-end', 'front@gmail.com', 'senhas001', type='f', company_or_user='usuário qualquer')
        self.users_api = APIUser.objects.filter(email='front@gmail.com')
        self.user_api_id = self.users_api.get().pk
        self.data = {
            'email': 'new-email@gmail.com',
            'password': 'new-password01',
            'type': 'm',
            'company_or_user': 'novo usuário'
        }

    def test_api_user_put_status_404(self):
        """Deve-se retornar status 404 ao tentar atualizar qualquer instância de api-users"""
        response = self.client.put(f'/api-users/{self.user_api_id}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_user_put_not_alter_in_data_base(self):
        """Os dados de api-users não devem ser modificados no banco de dados com requisições PUT"""
        self.client.put(f'/api-users/{self.user_api_id}/', self.data)
        self.assertTrue(self.users_api.exists())

