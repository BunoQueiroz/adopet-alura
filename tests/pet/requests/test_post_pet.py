from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from pet.models import Pet

class PetPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter = Shelter.objects.create(
            id=100, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        self.data_status_401 = {
            'id': 5,
            'name': 'Meu pet',
            'age': '2 semanas',
            'characteristics': 'Rápido e divertido',
            'size': 'Médio',
            'shelter': 100,
        }
        self.data_created_success = {
            'id': 6,
            'name': 'Meus pets',
            'age': '3 semanas',
            'characteristics': 'Rápido apenas',
            'size': 'grande',
            'shelter': 100,
        }

    def test_pet_post_status_401(self):
        """O status code retornado, quando um novo pet requisitado por um usuário anônimo, deve ser 401"""
        response = self.client.post('/pets/', self.data_status_401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_pet_post_created_in_data_base(self):
        """requisições POST, feita por usuários anônimos, não devem alterar o banco de dados"""
        self.client.post('/pets/', self.data_created_success)
        pet_request = Pet.objects.filter(name='Meus pets').exists()
        self.assertFalse(pet_request)
