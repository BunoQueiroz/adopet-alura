from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterPasswordValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_short_password = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas',
            'confirm_password': 'senhas',
            'email': 'email1234@gmail.com'
        })
        self.shelter_different_passwords = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas4002',
            'confirm_password': 'senhas190190',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_only_letters = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'SenhasComLetras',
            'confirm_password': 'SenhasComLetras',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_only_numbers = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': '12345678',
            'confirm_password': '12345678',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_only_small_letters = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'letrasminusculas',
            'confirm_password': 'letrasminusculas',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_small_letters_and_numbers = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'letras1234minusculas',
            'confirm_password': 'letras1234minusculas',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_only_capital_letters = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'SENHAMAIUSCULA',
            'confirm_password': 'SENHAMAIUSCULA',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_with_capital_letters_and_numbers = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'SENHA1234MAIUSCULA',
            'confirm_password': 'SENHA1234MAIUSCULA',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_very_strong = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'Pass123#!@-+word',
            'confirm_password': 'Pass123#!@-+word',
            'email': 'email1234@gmail.com'
        })
        self.shelter_password_strong = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'Pass123word',
            'confirm_password': 'Pass123word',
            'email': 'email1234@gmail.com'
        })

    def test_shelter_short_password(self):
        """Senhas com menos de 8 dígitos são consideradas inválidas"""
        self.assertFalse(self.shelter_short_password.is_valid())
    
    def test_shelter_different_passwords(self):
        """As senhas devem ser iguais, no serializer de abrigo, para serem válidas"""
        self.assertFalse(self.shelter_different_passwords.is_valid())
    
    def test_shelter_password_with_only_capita_and_small_letters(self):
        """As senhas com apenas letras maiúsculas e minúsculas são inválidas"""
        self.assertFalse(self.shelter_password_with_only_letters.is_valid())

    def test_shelter_password_with_only_small_letters(self):
        """As senhas com apenas letras minúsculas são inválidas"""
        self.assertFalse(self.shelter_password_with_only_small_letters.is_valid())
    
    def test_shelter_password_with_only_capital_letters(self):
        """As senhas com apenas letras maiúsculas são inválidas"""
        self.assertFalse(self.shelter_password_with_only_capital_letters.is_valid())
    
    def test_shelter_password_with_small_letters_and_numbers(self):
        """As senhas com apenas números e letras minúsculas são inválidas"""
        self.assertFalse(self.shelter_password_with_small_letters_and_numbers.is_valid())
    
    def test_shelter_password_with_capital_letters_and_numbers(self):
        """As senhas com apenas números e letras maiúsculas são inválidas"""
        self.assertFalse(self.shelter_password_with_capital_letters_and_numbers.is_valid())
    
    def test_shelter_password_with_only_numbers(self):
        """As senhas com apenas números são inválidas"""
        self.assertFalse(self.shelter_password_with_only_numbers.is_valid())
    
    def test_shelter_password_very_strong(self):
        """Senhas com letras maiúsculas e minúsculas, números e caracteres especiais devem ser válida"""
        self.assertTrue(self.shelter_password_very_strong.is_valid())

    def test_shelter_password_strong(self):
        """Senhas com letras maiúsculas e minúsculas e números devem ser válida"""
        self.assertTrue(self.shelter_password_strong.is_valid())
