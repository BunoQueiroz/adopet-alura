from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.data_shelter_post_id_200 = {
            'name': 'Abrigos diferentes',
            'road': 'Rua Nova Alegria',
            'number': '03',
            'borhood': 'Bendita',
            'CEP': '65685-000',
            'city': 'Paraipaba',
            'state': 'CE',
        }
        self.data_shelter_post_id_201 = {
            'name': 'Abrigo diferente',
            'road': 'Rua Nova Alegria',
            'number': '03',
            'borhood': 'Bendita',
            'CEP': '65685-000',
            'city': 'Paraipaba',
            'state': 'CE',
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
