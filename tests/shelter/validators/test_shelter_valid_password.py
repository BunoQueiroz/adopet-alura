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
            'password': 'senhascomletras',
            'confirm_password': 'senhascomletras',
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
        self.shelter_password_strong = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'pass123#!@-+word',
            'confirm_password': 'pass123#!@-+word',
            'email': 'email1234@gmail.com'
        })

    def test_shelter_short_password(self):
        """Senhas com menos de 8 dígitos são consideradas inválidas"""
        self.assertFalse(self.shelter_short_password.is_valid())
    
    def test_shelter_different_passwords(self):
        """As senhas devem ser iguais, no serializer de abrigo, para serem válidas"""
        self.assertFalse(self.shelter_different_passwords.is_valid())
    
    def test_shelter_password_with_only_letters(self):
        """As senhas com apenas letras são inválidas"""
        self.assertFalse(self.shelter_password_with_only_letters.is_valid())

    def test_shelter_password_with_only_numbers(self):
        """As senhas com apenas números são inválidas"""
        self.assertFalse(self.shelter_password_with_only_numbers.is_valid())
    
    def test_shelter_password_strong(self):
        """Senhas com letras, números e caracteres especiais deve ser válida"""
        self.assertTrue(self.shelter_password_strong.is_valid())

