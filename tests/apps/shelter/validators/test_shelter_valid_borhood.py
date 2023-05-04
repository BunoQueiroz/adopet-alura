from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterBorhoodValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.borhood_with_number = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': '1Borhood2',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
        })
        self.borhood_name_with_few_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Bo',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
        })
        self.borhood_with_special_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': '[^~`´.,<>:;-+*/\]Borhood(*&_+=!@#)',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
        })
        self.borhood_blank = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': '',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
        })
        self.borhood_valid = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'borhood': 'Boa Vista',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
        })

    def test_borhood_with_number(self):
        """Não é permitida a utilização de números na nomenclatura dos BAIRROS"""
        self.assertFalse(self.borhood_with_number.is_valid())
    
    def test_borhood_with_few_characters(self):
        """O nome de um BAIRRO deve ter pelo menos 3 caracteres"""
        self.assertFalse(self.borhood_name_with_few_characters.is_valid())
    
    def test_special_characters_in_borhood(self):
        """Não são permitidos caracteres especiais nos nomes dos BAIRROS"""
        self.assertFalse(self.borhood_with_special_characters.is_valid())

    def test_borhood_blank(self):
        """É permitido que os campos de bairro não sejam preenchidos"""
        self.assertTrue(self.borhood_blank.is_valid())

    def test_valid_borhood(self):
        """Estes exemplos de bairros devem ser considerados válidos"""
        self.assertTrue(self.borhood_valid.is_valid())
