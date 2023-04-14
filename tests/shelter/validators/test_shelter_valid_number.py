from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterBorhoodValidTestCase(APITestCase):
    def setUp(self) -> None:
        self.number_with_letter = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': '1n0',
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        })
        self.number_negative = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': -1,
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        })
        self.number_greater_then_9999 = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 10000,
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        })
        self.number_float = ShelterSerializer(data={
            'name': 'Nome do Abrigo',
            'road': 'Rua Válida',
            'number': 1.1,
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        })
        self.number_blank = ShelterSerializer(data={
            'name': 'Nome Abrigo',
            'road': 'Rua tal',
            'number': '',
            'borhood': 'Boa Vista',
            'CEP': '62685-000',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        })

    def test_number_in_string_format(self):
        """Não são permitidos NÚMEROS juntamente com letras"""
        self.assertFalse(self.number_with_letter.is_valid())
    
    def test_negative_number(self):
        """Não são permitidos NÚMEROS menores que 0"""
        self.assertFalse(self.number_negative.is_valid())
    
    def test_very_big_number(self):
        """Não são permitidos NÚMEROS que excedam 4 dígitos"""
        self.assertFalse(self.number_greater_then_9999.is_valid())

    def test_float_number(self):
        """Não são permitidos NÚMEROS de ponto flutuante"""
        self.assertFalse(self.number_float.is_valid())

    def test_blank_number(self):
        """Números de residências não são obrigatórios"""
        self.assertTrue(self.number_blank.is_valid())
