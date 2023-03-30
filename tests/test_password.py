from django.test import TestCase
from tutor.models import Tutor
from tutor.serializers import TutorSerializer

class PasswordTestCase(TestCase):
    def setUp(self):
        self.tutor_serializer_one = TutorSerializer(data={
            'full_name': 'test1',
            'password': 'test1234',
            'email': 'email@email.com',
            'confirm_password': 'test1234'
        })
        self.tutor_serializer_two = TutorSerializer(data={
            'full_name': 'test2',
            'password': 'testdois',
            'email': 'email@email.com',
            'confirm_password': 'testdois'
        })
        self.tutor_serializer_tree = TutorSerializer(data={
            'full_name': 'test3',
            'password': '12345678',
            'email': 'email@email.com',
            'confirm_password': '12345678'
        })
        self.tutor_serializer_four = TutorSerializer(data={
            'full_name': 'test4',
            'password': 'test154',
            'email': 'email@email.com',
            'confirm_password': 'test154'
        })

        self.tutor_serializer_five = TutorSerializer(data={
            'full_name': 'test5',
            'password': 'differents_passwords2',
            'email': 'email@email.com',
            'confirm_password': 'differents_passwords3'
        })

    def test_password_stronger(self):
        """Verifica se as senhas com número e letras, além de possuírem pelo menos 8 caracteres, estão passando"""
        self.assertEqual(True, self.tutor_serializer_one.is_valid())

    def test_password_not_number(self):
        """Verifica se as senhas que contém somente letras NÃO estão passando"""
        self.assertEqual(False, self.tutor_serializer_two.is_valid())
    
    def test_password_not_letter(self):
        """Verifica se as senhas que contém somente números NÃO estão passando"""
        self.assertEqual(False, self.tutor_serializer_tree.is_valid())
    
    def test_short_passwords(self):
        """Verifica se as senhas com menos de 8 caracteres NÃO estão passando"""
        self.assertEqual(False, self.tutor_serializer_four.is_valid())

    def test_different_passwords(self):
        """Verifica se as senhas diferentes da confirmação NÃO estão passando"""
        self.assertEqual(False, self.tutor_serializer_five.is_valid())

