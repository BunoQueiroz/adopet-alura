from rest_framework.test import APITestCase
from tutor.models import Tutor
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

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
            'password': 'password01',
            'confirm_password': 'password01',
        }
        self.head = {
        }

    def test_username_equal_email_tutor(self):
        """Garante que os usernames dos tutores sejam seus próprios emails"""
        self.client.post(path='/tutors/', data=self.data)
        tutor_in_data_base = Tutor.objects.get(email=self.data['email'])
        self.assertEqual(tutor_in_data_base.username, self.email)
