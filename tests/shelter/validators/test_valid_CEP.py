from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterCEPValidTestCase(APITestCase):
    def setUp(self) -> None:
        self.shelter_cep_valid_format = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65548-123',
            'city': 'city valid',
            'state': 'state',
        })
        self.shelter_cep_invalid_format = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '65-548123',
            'city': 'city valid',
            'state': 'state',
        })
        self.shelter_cep_with_letter = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '6554p-123',
            'city': 'city valid',
            'state': 'state',
        })
        self.shelter_cep_without_hyphen = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'road': 'Rua Valid',
            'number': 1,
            'borhood': 'Borhood',
            'CEP': '655488123',
            'city': 'city valid',
            'state': 'state',
        })

    def test_valid_CEP_format(self):
        """Verifica se o CEP está no formato adequado"""
        self.assertTrue(self.shelter_cep_valid_format.is_valid())
        self.assertFalse(self.shelter_cep_invalid_format.is_valid())
        self.assertFalse(self.shelter_cep_with_letter.is_valid())
        self.assertFalse(self.shelter_cep_without_hyphen.is_valid())
