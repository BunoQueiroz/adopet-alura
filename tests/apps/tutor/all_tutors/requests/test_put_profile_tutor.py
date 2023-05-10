from rest_framework.test import APITestCase
from django.urls import reverse
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token


class ProfileTutorPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_register = Tutor.objects.create_user('tutor1', 'tutor1@gmail.com', 'Senha004', full_name='Tutor')
        self.url = reverse('tutor-profiles-list')
        self.data = {}

    def test_profile_tutor_put_status_401(self):
        """Qualquer usuário não autenticado não pode ver os perfis de tutores"""
        response = self.client.put(f'{self.url}{self.tutor_register.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class ProfileTutorPUTRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_any = Tutor.objects.create_user(
            'tutor_any', 'email@tutor.com', 'Senha001', full_name='Tutor qualquer'
        )
        self.token = Token.objects.create(user=self.tutor_any)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')        
        self.url = reverse('tutor-profiles-list')
        self.data = {
            'full_name': 'Novo Nome',
            'email': 'emails@gmail.com',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
        }

    def test_profile_tutor_athenticated_put_status_200(self):
        """Tutores autenticados devem ter como status code, de resposta a requisição, 200"""
        response = self.client.put(f'{self.url}{self.tutor_any.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#TODO: Criar testes para requisições PATCH e Apagar os testes não mais covenientes dos recursos de tutor e abrigo