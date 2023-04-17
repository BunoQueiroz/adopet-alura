from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.data_shelter_post_id_200 = {
            'name': 'Abrigos diferentes',
            'password': 'senhas001',
            'email': 'emails@gmail.com',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        }
        self.data_shelter_post_id_201 = {
            'name': 'Abrigo diferente',
            'password': 'senhas001',
            'email': 'emails@gmail.com',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        }
    
    def test_post_status_201(self):
        """O Status de Abrigo criado deve ser 201"""
        response = self.client.post('/shelters/', self.data_shelter_post_id_201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_insert_in_data_base(self):
        """Os dados passados devem ser, de fato, criados no banco de dados"""
        self.client.post('/shelters/', self.data_shelter_post_id_200)
        shelter_exists = Shelter.objects.filter(name='Abrigos diferentes').exists()
        self.assertTrue(shelter_exists)
