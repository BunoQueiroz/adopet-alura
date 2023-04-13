from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from pet.models import Pet

class PetPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter = Shelter.objects.create(
            id=100, name='Abrigo Um', road='Rua João Naciso de Oliveira', number='03', borhood='Pedrinhas', CEP='62685-000', city='Paraipaba', state='CE',
        )
        self.data_status_201 = {
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

    def test_pet_post_status_201(self):
        """O status code restornado, quando um novo pet for criado, deve ser 201"""
        response = self.client.post('/pets/', self.data_status_201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_pet_post_created_in_data_base(self):
        """O pet requisitado (POST) deve ser inserido, de fato, no banco de dados"""
        self.client.post('/pets/', self.data_created_success)
        pet_request = Pet.objects.filter(name='Meus pets').exists()
        self.assertTrue(pet_request)
