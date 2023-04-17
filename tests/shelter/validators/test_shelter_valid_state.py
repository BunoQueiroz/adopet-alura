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
            'password': 'senhas001',
            'state': 'A',
        })
        self.state_with_tree_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
            'state': 'abc',
        })
        self.state_with_special_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
            'state': '%")(*&¨%$#@!-+*;.,|\/',
        })
        self.state_with_number = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Borhood',
            'city': 'city valid',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
            'state': 'a7',
        })

    def test_exact_two_character_state(self):
        """Somente são considerados válidos estados com dois caracteres 'maiúsculos' EX.: CE"""
        self.assertFalse(self.state_with_one_characters.is_valid())
        self.assertFalse(self.state_with_tree_characters.is_valid())

    def test_number_or_especial_characters(self):
        """Não são permitidos números ou Caracteres especiais de qualquer tipo"""
        self.assertFalse(self.state_with_special_characters.is_valid())
        self.assertFalse(self.state_with_number.is_valid())
