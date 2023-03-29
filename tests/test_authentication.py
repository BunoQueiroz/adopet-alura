from django.test import TestCase
from tutor.models import Tutor
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('bruno', 'b@gmail.com', 'bruno')
        self.tutor_one = Tutor.objects.create_user(full_name='fernando henrique cardoso', username='fernando', password='fernando')
        
    def test_authenticacao_basica_para_os_tutores(self):
        result = authenticate(username='fernando', password='fernando')
        self.assertIsNotNone(result)

    def test_authenticacao_usuarios_no_geral(self):
        result = authenticate(username='bruno', password='bruno')
        self.assertIsNotNone(result)
    