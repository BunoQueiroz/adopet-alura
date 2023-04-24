from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterCityValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.city_with_number_in_name = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'borhood': 'Borhood',
            'city': 'city 1nvalid',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })
        self.city_with_name_short = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'borhood': 'Borhood',
            'city': 'CEP',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })
        self.city_especial_charcarters = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'borhood': 'Borhood',
            'city': 'city%$ !nvalid@#)(+=}{;.,<>\/',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })
        self.city_graphic_accents = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'borhood': 'Borhood',
            'city': 'São Amapá Uchôa',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })

    def test_city_with_number(self):
        """Cidades com números em seus nomes não são válidas"""
        self.assertFalse(self.city_with_number_in_name.is_valid())

    def test_city_min_size_name(self):
        """Não são permitidas cidades que tenham nome com menos de 4 caracteres"""
        self.assertFalse(self.city_with_name_short.is_valid())

    def test_city_with_specials_characters(self):
        """Cidades com caracteres especiais são inválidas, exceto com underline e/ou ífem (_ e -)"""
        self.assertFalse(self.city_especial_charcarters.is_valid())

    def test_city_with_grafic_accents(self):
        """Acentuações gráficas nos nomes de cidade devem ser permitidas"""
        self.assertTrue(self.city_graphic_accents.is_valid())
