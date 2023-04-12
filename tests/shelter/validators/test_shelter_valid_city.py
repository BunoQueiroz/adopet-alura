from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterCityValidTestCase(APITestCase):
    def setUp(self) -> None:
        self.city_with_number_in_name = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city 1nvalid',
            'state': 'CE',
        })
        self.city_with_name_short = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'CEP',
            'state': 'CE',
        })
        self.city_especial_charcarters = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city%$ !nvalid@#)(+=}{;.,<>\/',
            'state': 'CE',
        })
        self.city_graphic_accents = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'São Amapá Uchôa',
            'state': 'CE',
        })

    def test_city_with_number(self):
        """Cidades com números em seus nomes não são válidas"""
        self.assertFalse(self.city_with_number_in_name.is_valid())

    def test_city_min_size_name(self):
        """Não são permitidas cidades que tenham nome com menos de 4 caracteres"""
        self.assertFalse(self.city_with_name_short.is_valid())

    def test_city_with_specials_characters(self):
        """Não aceita caracteres especiais, exceto underline e ífem (_ e -)"""
        self.assertFalse(self.city_especial_charcarters.is_valid())

    def test_grafic_accents(self):
        """Permite que seja possível usar acentuações gráficas nos nomes de cidade"""
        self.assertTrue(self.city_graphic_accents.is_valid())
