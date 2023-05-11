from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token


class TutorsProfilePOSTRequestsTestCase(APITestCase):

    def setUp(self):
        self.data = {
            'full_name': 'tutor test post',
            'email': 'new-email@email.com',
            'password': 'NewPassword01',
            'confirm_password': 'NewPassword01',
        }
        self.tutor_one = Tutor.objects.create_user(
            'test post', 'post@email.com', 'testpost01', full_name='test post', pk=100
        )
        self.url = reverse('tutors-list')

    def test_post_tutor_profile_by_anonymous_users_status_404(self):
        """Requisições POST, feita por usuários anônimos ao recurso de perfil de tutores, deve retornar status 404"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_post_tutor_profile_by_anonymous_users_in_data_base(self):
        """Usuários anônimos não devem conseguir inserir novos tutores no banco de dados"""
        self.client.post(self.url, self.data)
        new_tutor_expected = Tutor.objects.filter(email='new-email@email.com').exists()
        self.assertFalse(new_tutor_expected)


class TutorsProfilePOSTRequestsAuthenticatedTestCase(APITestCase):

    def setUp(self):
        self.data = {
            'full_name': 'tutor test post',
            'email': 'new-email@email.com',
            'password': 'NewPassword01',
            'confirm_password': 'NewPassword01',
        }
        self.tutor_authenticated = Tutor.objects.create_user(
            'test post', 'post@email.com', 'testpost01', full_name='test post', pk=100
        )
        self.token = Token.objects.create(user=self.tutor_authenticated)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.url = reverse('tutors-list')

    def test_post_tutor_profile_by_user_authenticated_status_201(self):
        """Requisições POST, feita por tutores autenticados ao recurso de perfil de tutores, deve retornar status 201"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_post_tutor_profile_by_user_authenticated_in_data_base(self):
        """Tutores autenticados devem conseguir inserir novos tutores no banco de dados"""
        self.client.post(self.url, self.data)
        new_tutor_expected = Tutor.objects.filter(email='new-email@email.com').exists()
        self.assertTrue(new_tutor_expected)
