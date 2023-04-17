from rest_framework.test import APITestCase
from pet.models import Pet
from rest_framework import status
from shelter.models import Shelter

class PetGETRequestsTestCase(APITestCase):
    
    def setUp(self) -> None:
        shelter = Shelter.objects.create(
            id=100, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        Pet.objects.create(
            id=1, name='São bernardo', age='2 anos', size='grande', shelter=shelter, characteristics='Divertido e elétrico'
        )

    def test_pet_get_status_200(self):
        """O Status code retornado, quando for enviada uma requisição get, deve ser 200"""
        response = self.client.get('/pets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pet_get_format_JSON(self):
        """O conteúdo do recurso de pet deve ser retornado em formato JSON"""
        response = self.client.get('/pets/')
        self.assertEqual(response['Content-Type'], 'application/json')
    
    def test_pet_get_for_id_status_200(self):
        """O Status code retornado, ao requisitar (get) um pet pelo ID, deve ser 200"""
        response = self.client.get('/pets/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pet_get_for_id_format_JSON(self):
        """O conteúdo de um recurso de pet, por ID, deve ser retornado em formato JSON"""
        response = self.client.get('/pets/1/')
        self.assertEqual(response['Content-Type'], 'application/json')
    