from rest_framework.test import APITestCase
from django.urls import reverse
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token


class AllTutorsGETRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_register = Tutor.objects.create_user('tutor1', 'tutor1@gmail.com', 'Senha004', full_name='Tutor')
        self.url = reverse('all-tutors')

    def test_all_tutors_get_status_200(self):
        """Qualquer usuário não autenticado pode ver todos os tutores cadastrados"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_tutors_get_by_id_status_404(self):
        """Qualquer usuário não autenticado não pode ver qualquer tutor cadastrados por seu id"""
        response = self.client.get(f'{self.url}{self.tutor_register.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AllTutorsGETRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor_any = Tutor.objects.create_user(
            'tutor_any', 'email@tutor.com', 'Senha001', full_name='Tutor qualquer'
        )
        self.token = Token.objects.create(user=self.tutor_any)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')        
        self.url = reverse('all-tutors')

    def test_all_tutors_athenticated_get_status_200(self):
        """Tutores autenticados devem ter como status code, de resposta a requisição get à rota de todos os tutores, 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_all_tutors_athenticated_get_by_id_status_404(self):
        """Tutores, mesmo autenticados, devem ter como status code, de resposta a requisição get à rota tutores por id, 404"""
        response = self.client.get(f'{self.url}{self.tutor_any.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
