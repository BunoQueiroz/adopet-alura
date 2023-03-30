from django.test import TestCase
from tutor.serializers import TutorSerializer

class TutorPasswordTestCase(TestCase):
    def setUp(self):
        self.tutor_serializer_one = TutorSerializer(data={
            'full_name': 'test valid',
            'password': 'test1234',
            'email': 'email@email.com',
            'confirm_password': 'test1234'
        })
        self.tutor_serializer_two = TutorSerializer(data={
            'full_name': 'tests two',
            'password': 'testdois',
            'email': 'email@email.com',
            'confirm_password': 'testdois'
        })
        self.tutor_serializer_tree = TutorSerializer(data={
            'full_name': 'tests tree',
            'password': '12345678',
            'email': 'email@email.com',
            'confirm_password': '12345678'
        })
        self.tutor_serializer_four = TutorSerializer(data={
            'full_name': 'tests four',
            'password': 'test154',
            'email': 'email@email.com',
            'confirm_password': 'test154'
        })

        self.tutor_serializer_five = TutorSerializer(data={
            'full_name': 'tests five',
            'password': 'differents_passwords2',
            'email': 'email@email.com',
            'confirm_password': 'differents_passwords3'
        })

    def test_password_stronger(self):
        """Verifica se as senhas com número e letras, além de possuírem pelo menos 8 caracteres, estão passando"""
        self.assertTrue(self.tutor_serializer_one.is_valid())

    def test_password_not_number(self):
        """Verifica se as senhas que contém somente letras NÃO estão passando"""
        self.assertFalse(self.tutor_serializer_two.is_valid())
    
    def test_password_not_letter(self):
        """Verifica se as senhas que contém somente números NÃO estão passando"""
        self.assertFalse(self.tutor_serializer_tree.is_valid())
    
    def test_short_passwords(self):
        """Verifica se as senhas com menos de 8 caracteres NÃO estão passando"""
        self.assertFalse(self.tutor_serializer_four.is_valid())

    def test_different_passwords(self):
        """Verifica se as senhas diferentes da confirmação NÃO estão passando"""
        self.assertFalse(self.tutor_serializer_five.is_valid())

