from rest_framework.test import APITestCase
from django.urls import reverse
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token


class allTutorsPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_register = Tutor.objects.create_user('tutor1', 'tutor1@gmail.com', 'Senha004', full_name='Tutor', pk=20)
        self.url = reverse('all-tutors')
        self.data = {
            'email': 'new-email@gmail.com',
            'password': 'NovaSenha01',
            'confirm_password': 'NovaSenha01',
            'full_name': 'Meu Nome Completo'
        }

    def test_all_tutors_put_status_404(self):
        """Qualquer usuário não autenticado não pode alterar qualquer intância de tutores"""
        response = self.client.put(f'{self.url}{self.tutor_register.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_all_tutors_put_in_data_base(self):
        """Qualquer usuário não autenticado não pode alterar qualquer a base de relacionada aos tutores"""
        self.client.put(f'{self.url}{self.tutor_register.pk}/', self.data)
        current_tutor = Tutor.objects.get(pk=20)
        self.assertEqual(current_tutor.email, 'tutor1@gmail.com')


class allTutorsPUTRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_any = Tutor.objects.create_user(
            'tutor_any', 'email@tutor.com', 'Senha001', full_name='Tutor qualquer', pk=21
        )
        self.token = Token.objects.create(user=self.tutor_any)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')        
        self.url = reverse('all-tutors')
        self.data = {
            'full_name': 'Novo Nome',
            'email': 'emails@gmail.com',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
        }

    def test_all_tutor_athenticated_put_by_id_status_404(self):
        """Mesmo Tutores autenticados devem ter como status code, de resposta a requisição put à um tutor por id, 404"""
        response = self.client.put(f'{self.url}{self.tutor_any.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_all_tutor_athenticated_put_in_data_base(self):
        """Mesmo Tutores autenticados não devem conseguir alterar o banco de dados realizando requisições put ao id de qualquer tutor"""
        self.client.put(f'{self.url}{self.tutor_any.pk}/', self.data)
        current_tutor = Tutor.objects.get(pk=21)
        self.assertEqual(current_tutor.email, 'email@tutor.com')
