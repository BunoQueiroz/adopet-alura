from django.test import TestCase
from tutor.models import Tutor
from django.contrib.auth import authenticate

class TutorAuthenticationTestCase(TestCase):

    def setUp(self):
        self.tutor_one = Tutor.objects.create_user(full_name='fernando henrique cardoso', username='fernando', password='fernando')
        
    def test_tutor_basic_authentication_for_tutors(self):
        """As autenticações devem ocorrer de maneira correta com os tutores cadastrados"""
        result = authenticate(username='fernando', password='fernando')
        self.assertIsNotNone(result)

    def test_tutor_unregistered_tutor_authentication(self):
        """As autenticações de tutores não cadastrados não devem ocorrer"""
        tutor_result = authenticate(username='tutor', password='tutor1234')
        null_result = authenticate(username='', password='')
        self.assertIsNone(tutor_result)
        self.assertIsNone(null_result)
        
    def test_tutor_unregistered_users_authentication(self):
        """As autenticações de usuários não cadastrados não ocorrão de forma alguma"""
        admin_result = authenticate(username='admin', password='admin1234')
        null_result = authenticate(username='', password='')
        self.assertIsNone(admin_result)
        self.assertIsNone(null_result)
