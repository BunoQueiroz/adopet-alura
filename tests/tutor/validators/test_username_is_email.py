from rest_framework.test import APITestCase
from tutor.models import Tutor

class UsernameIsEmailTestCase(APITestCase):
    def setUp(self):
        self.email = 'first_email@gmail.com'
        self.data = {
            'id': 201,
            'full_name': 'Brunos Castros',
            'email': 'first_email@gmail.com',
            'password': 'password01',
            'confirm_password': 'password01'
        }

    def test_username_equal_email(self):
        """Garante que os usernames dos tutores sejam seus próprios emails"""
        self.client.post('/tutors/', self.data)
        tutor_in_data_base = Tutor.objects.get(email=self.data['email'])
        self.assertEqual(tutor_in_data_base.username, self.email)
