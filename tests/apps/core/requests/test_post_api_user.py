from rest_framework.test import APITestCase
from rest_framework import status
from core.models import APIUser


class APIUserPostRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'email': 'emailapi@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'company_or_user': 'usuário qualquer',
            'type': 'm',
        }
        self.users_api = APIUser.objects.filter(email='emailapi@gmail.com')

    def test_api_user_post_status_201(self):
        """O status 201 deve ser retornado ao tentar incluir um novo api_user, mesmo sendo um usuário anônimo"""
        response = self.client.post('/api-users/', self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_user_register_new_user_in_data_base(self):
        """Deve-se incluir novos api_users, de fato, no banco de dados"""
        self.client.post('/api-users/', self.data)
        self.assertTrue(self.users_api.exists())
