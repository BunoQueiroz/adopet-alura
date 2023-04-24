from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterNameValidTestCase(APITestCase):

    def setUp(self):
        self.shelter_valid_name = ShelterSerializer(data={
            'name': 'Shelter@ & Valid-123ração',
            'borhood': 'Borhood',
            'city': 'city valid',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })        
        self.shelter_invalid_name = ShelterSerializer(data={
            'name': '1234-&@$56',
            'borhood': 'Borhood',
            'city': 'city valid',
            'state': 'CE',
            'phone': '',
            'email': 'email@gmail.com',
            'password': 'senhas001',
        })
    
    def test_shelter_valid_name(self):
        """Um nome de abrigo que possue letras e números, além de alguns caracteres especiais, seja válido"""
        self.assertTrue(self.shelter_valid_name.is_valid())

    def test_shelter_name_without_letters(self):
        """Não permite nome de abrigo sem pelo menos 1 letra"""
        self.assertFalse(self.shelter_invalid_name.is_valid())
