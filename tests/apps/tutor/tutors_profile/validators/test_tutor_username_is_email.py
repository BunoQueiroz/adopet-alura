from rest_framework.test import APITestCase
from tutor.models import Tutor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse


class TutorUsernameIsEmailTestCase(APITestCase):
    
    def setUp(self):
        self.email = 'first_email@gmail.com'
        self.user = User.objects.create_superuser(email='meuemail@gmail.com', username='bruno', password='bruno001')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.data = {
            'id': 201,
            'full_name': 'Brunos Castros',
            'email': 'first_email@gmail.com',
            'password': 'Password01',
            'confirm_password': 'Password01',
        }
        self.url = reverse('tutors-list')

    def test_tutor_username_equal_email(self):
        """Garante que os usernames dos tutores sejam seus próprios emails"""
        self.client.post(self.url, self.data)
        tutor_in_data_base = Tutor.objects.get(email=self.data['email'])
        self.assertEqual(tutor_in_data_base.username, self.email)
