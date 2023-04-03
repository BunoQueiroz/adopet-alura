from django.test import TestCase
from tutor.models import Tutor
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('bruno', 'b@gmail.com', 'bruno')
        self.tutor_one = Tutor.objects.create_user(full_name='fernando henrique cardoso', username='fernando', password='fernando')
        
    def test_basic_authentication_for_tutors(self):
        """Verifica se as autenticações estão ocorrendo de maneira correta com os tutores cadastrados"""
        result = authenticate(username='fernando', password='fernando')
        self.assertIsNotNone(result)

    def test_authentication_users_in_general(self):
        """Verifica se as autenticações de usuários (sem nomenclatura específica) estão acontecendo corretamente"""
        result = authenticate(username='bruno', password='bruno')
        self.assertIsNotNone(result)
    
    def test_unregistered_tutor_authentication(self):
        """Verifica se as autenticações de tutores não cadastrados não estão ocorrendo"""
        tutor_result = authenticate(username='tutor', password='tutor1234')
        null_result = authenticate(username='', password='')
        self.assertIsNone(tutor_result)
        self.assertIsNone(null_result)
        
    def test_unregistered_users_authentication(self):
        """Verifica se as autenticações de usuários não cadastrados não ocorrão de forma alguma"""
        admin_result = authenticate(username='admin', password='admin1234')
        null_result = authenticate(username='', password='')
        self.assertIsNone(admin_result)
        self.assertIsNone(null_result)

