from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterStateValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.state_with_one_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': 'A',
        })
        self.state_with_tree_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': 'abc',
        })
        self.state_with_special_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': '%")(*&¨%$#@!-+*;.,|\/',
        })
        self.state_with_number = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': 'a7',
        })
        self.state_without_capital_letter = ShelterSerializer(data={
            'name': 'Nome dos Abrigos',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': 'ce',
        })
        self.state_with_one_capital_letter = ShelterSerializer(data={
            'name': 'Nome dos Abrigos',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'state': 'Ce',
        })

    def test_state_exact_two_character(self):
        """Somente são considerados válidos estados com dois caracteres 'maiúsculos' EX.: CE"""
        self.assertFalse(self.state_with_one_characters.is_valid())
        self.assertFalse(self.state_with_tree_characters.is_valid())

    def test_state_number_or_especial_characters(self):
        """Não são permitidos números ou caracteres especiais de qualquer tipo no campo de estado"""
        self.assertFalse(self.state_with_special_characters.is_valid())
        self.assertFalse(self.state_with_number.is_valid())
    
    def test_state_capital_letters(self):
        """Somente são permitidas letras maiúsculas no campo de estado"""
        self.assertFalse(self.state_without_capital_letter.is_valid())
        self.assertFalse(self.state_with_one_capital_letter.is_valid())
