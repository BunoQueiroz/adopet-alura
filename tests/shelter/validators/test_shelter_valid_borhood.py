from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterBorhoodValidTestCase(APITestCase):
    def setUp(self) -> None:
        self.borhood_with_number = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 10,
            'borhood': '1Borhood2',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
        })
        self.borhood_name_with_few_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 12,
            'borhood': 'Bo',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
        })
        self.borhood_with_special_characters = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 11,
            'borhood': '[^~`´.,<>:;-+*/\]Borhood(*&_+=!@#)',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
        })
        self.borhood_blank = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 10,
            'borhood': '',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
        })
        self.borhood_valid = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 10,
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
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

    def test_blank(self):
        """É permitido que os campos de bairro não sejam preenchidos"""
        self.assertTrue(self.borhood_valid.is_valid())

    def test_valid_borhood(self):
        """Exemplo de BAIRRO que deve ser considerado válido"""
        self.assertTrue(self.borhood_valid.is_valid())
