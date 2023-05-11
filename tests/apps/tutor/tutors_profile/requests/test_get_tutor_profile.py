from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token


class TutorsProfileGETRequestsTestCase(APITestCase):

    def setUp(self):
        self.fields_data_tutor_one = {
            'id': 1,
            'full_name': 'tutor test',
            'email': 'email@email.com',
        }
        self.tutor_one = Tutor.objects.create_user(
            'tutor test', 'email@email.com', 'password01', full_name='tutor test', pk=1
        )
        self.url = reverse('tutors-list')

    def test_request_get_tutors_profile_return_status_404(self):
        """Verifica se as requisições para pegar perfil de tutores está retornando STATUS 404"""
        response = self.client.get({self.url})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_request_get_tutors_profile_by_id(self):
        """As requisições para pegar perfil tutores por ID deve retornar STATUS 404"""
        response = self.client.get(f'{self.url}{self.tutor_one.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TutorsProfileGETRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self):
        self.fields_data_tutor_one = {
            'id': 102,
            'full_name': 'tutor test',
            'email': 'email@email.com',
        }
        self.tutor_any = Tutor.objects.create_user(
            'tutor test', 'email@email.com', 'password01', full_name='tutor test', pk=102
        )
        self.token = Token.objects.create(user=self.tutor_any)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.url = reverse('tutors-list')

    def test_render_data_tutors_profile_especific(self):
        """Os campos de perfil de tutor renderizado devem coincidir com os desejado (ID, FULL_NAME, EMAIL)"""
        response = self.client.get(f'{self.url}{self.tutor_any.auth_token}/')
        self.assertEqual(set(response.json()), set(self.fields_data_tutor_one))

    def test_render_data_tutors_profile_JSON_format(self):
        """O formato das respostas para pegar o perfil de um determinado tutor deve ser JSON"""
        response = self.client.get(f'{self.url}{self.tutor_any.auth_token}/')
        self.assertEqual(response['Content-Type'], 'application/json')
