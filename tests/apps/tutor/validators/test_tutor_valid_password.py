from django.test import TestCase
from tutor.serializers import TutorSerializer

class TutorPasswordValidTestCase(TestCase):

    def setUp(self):
        self.tutor_strong_password = TutorSerializer(data={
            'full_name': 'test valid',
            'password': 'test1234',
            'email': 'email@email.com',
            'confirm_password': 'test1234'
        })
        self.tutor_password_without_number = TutorSerializer(data={
            'full_name': 'tests two',
            'password': 'testdois',
            'email': 'email@email.com',
            'confirm_password': 'testdois'
        })
        self.tutor_password_without_letter = TutorSerializer(data={
            'full_name': 'tests tree',
            'password': '12345678',
            'email': 'email@email.com',
            'confirm_password': '12345678'
        })
        self.tutor_short_password = TutorSerializer(data={
            'full_name': 'tests four',
            'password': 'test154',
            'email': 'email@email.com',
            'confirm_password': 'test154'
        })
        self.tutor_differents_password = TutorSerializer(data={
            'full_name': 'tests five',
            'password': 'differents_passwords2',
            'email': 'email@email.com',
            'confirm_password': 'differents_passwords3'
        })

    def test_tutor_password_stronger(self):
        """As senhas com número e letras, além de possuírem pelo menos 8 caracteres, devem ser válidas"""
        self.assertTrue(self.tutor_strong_password.is_valid())

    def test_tutor_password_without_number(self):
        """As senhas que contém somente letras não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_without_number.is_valid())
    
    def test_tutor_password_not_letter(self):
        """As senhas que contém somente números não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_without_letter.is_valid())
    
    def test_tutor_password_short(self):
        """As senhas com menos de 8 caracteres não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_short_password.is_valid())

    def test_tutor_different_passwords(self):
        """As senhas diferentes da confirmação não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_differents_password.is_valid())
