from django.test import TestCase
from tutor.serializers import TutorSerializer


class TutorPasswordValidTestCase(TestCase):

    def setUp(self):
        self.tutor_strong_password = TutorSerializer(data={
            'full_name': 'test valid',
            'password': 'Test1234',
            'email': 'email@email.com',
            'confirm_password': 'Test1234'
        })
        self.tutor_password_very_strong = TutorSerializer(data={
            'full_name': 'test valid',
            'password': 'Test#@$!1234',
            'email': 'email@email.com',
            'confirm_password': 'Test#@$!1234'
        })
        self.tutor_password_with_only_letters = TutorSerializer(data={
            'full_name': 'tests tantofaz',
            'password': 'TestDois',
            'email': 'email@email.com',
            'confirm_password': 'TestDois'
        })
        self.tutor_password_with_only_small_letters = TutorSerializer(data={
            'full_name': 'tests tantofaz',
            'password': 'testdois',
            'email': 'email@email.com',
            'confirm_password': 'testdois'
        })
        self.tutor_password_with_only_capital_letters = TutorSerializer(data={
            'full_name': 'tests tantofaz',
            'password': 'TESTEDOIS',
            'email': 'email@email.com',
            'confirm_password': 'TESTEDOIS'
        })
        self.tutor_password_with_small_letters_and_numbers = TutorSerializer(data={
            'full_name': 'tests tantofaz',
            'password': 'teste1234',
            'email': 'email@email.com',
            'confirm_password': 'teste1234'
        })
        self.tutor_password_with_capital_letters_and_numbers = TutorSerializer(data={
            'full_name': 'tests tantofaz',
            'password': 'SENHA001',
            'email': 'email@email.com',
            'confirm_password': 'SENHA001'
        })
        self.tutor_password_with_only_numbers = TutorSerializer(data={
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
        """As senhas com número e letras maiúsculas e minúsculas, além de possuírem pelo menos 8 caracteres, devem ser válidas"""
        self.assertTrue(self.tutor_strong_password.is_valid())
    
    def test_tutor_password_very_stronger(self):
        """As senhas com número e letras maiúsculas e minúsculas, além 8 caracteres e caracteres especiais, devem ser válidas"""
        self.assertTrue(self.tutor_password_very_strong.is_valid())

    def test_tutor_password_with_only_letters(self):
        """As senhas que contém somente letras não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_only_letters.is_valid())
    
    def test_tutor_password_with_only_small_letters(self):
        """As senhas que contém somente letras minúsculas não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_only_small_letters.is_valid())
    
    def test_tutor_password_with_only_capital_letters(self):
        """As senhas que contém somente letras maiúsculas não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_only_capital_letters.is_valid())
    
    def test_tutor_password_with_small_letters_and_numbers(self):
        """As senhas que contém somente letras minúsculas e números não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_small_letters_and_numbers.is_valid())
    
    def test_tutor_password_with_capital_letters_and_numbers(self):
        """As senhas que contém somente letras maiúsculas e números não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_capital_letters_and_numbers.is_valid())
    
    def test_tutor_password_with_only_numbers(self):
        """As senhas que contém somente números não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_password_with_only_numbers.is_valid())
    
    def test_tutor_password_short(self):
        """As senhas com menos de 8 caracteres não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_short_password.is_valid())

    def test_tutor_different_passwords(self):
        """As senhas diferentes da confirmação não devem ser consideradas válidas"""
        self.assertFalse(self.tutor_differents_password.is_valid())
