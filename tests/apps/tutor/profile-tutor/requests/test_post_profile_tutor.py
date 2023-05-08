from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse


class ProfileTutorPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = Tutor.objects.create_user('tutor', 'emailtutor1@gmail.com', 'Senha001', full_name='Meu Nome')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.data = {}
        self.url = reverse('tutor-profiles-list')

    def test_profile_tutor_post_status_405(self):
        """O status code retornado, ao ser requisitado via (POST) o recurso de perfil de tutor, deve ser 405"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
