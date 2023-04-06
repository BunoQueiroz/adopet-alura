from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterRoadValidTestCase(APITestCase):
    def setUp(self) -> None:
        self.road_specials_characters = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Ru@ inválida',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city valid',
            'state': 'CE',
        })
        self.road_graphic_accents = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua João Fantástico Uchôa',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city valid',
            'state': 'CE',
        })
        self.road_number_in_name = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua 085 João Fantástico Uchôa',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city valid',
            'state': 'CE',
        })
        self.road_short_name = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city valid',
            'state': 'CE',
        })

    def test_specials_characters_in_road(self):
        """Impossível haver ruas brasileiras com certos caracteres especiais"""
        self.assertFalse(self.road_specials_characters.is_valid())

    def test_road_graphic_accents(self):
        """Permite a acentuação gráfica nos nomes das ruas (braileiras)"""
        self.assertTrue(self.road_graphic_accents.is_valid())
    
    def test_number_in_road_name(self):
        """Permite a utilização de números nos nomes das ruas (braileiras)"""
        self.assertTrue(self.road_number_in_name.is_valid())
    
    def test_road_short_name(self):
        """São permitidas somente ruas brasileiras com pelo menos 4 letras"""
        self.assertFalse(self.road_short_name.is_valid())
