from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse


class AllTutorsPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'email': 'new-email',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
            'full_name': 'Bruno Castro'
        }
        self.url = reverse('all-tutors')

    def test_all_tutors_post_status_401(self):
        """O status code retornado, ao ser requisitado via (POST) o recurso de tutor, deve ser 401"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class AllTutorsPOSTRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor = Tutor.objects.create_user(
            'tutor', 'emailtu@gmail.com', 'Senha001', full_name='Tutor Master'
        )
        self.token = Token.objects.create(user=self.tutor)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.data = {
            'email': 'new-email',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
            'full_name': 'Bruno Castro'
        }
        self.url = reverse('all-tutors')

    def test_all_tutors_post_authenticated_status_405(self):
        """O status code retornado, ao ser requisitado via (POST) o recurso de tutor por um tutor autenticado, deve ser 405"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
