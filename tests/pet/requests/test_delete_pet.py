from rest_framework.test import APITestCase
from pet.models import Pet
from rest_framework import status
from shelter.models import Shelter

class PetDELETERequestsTestCase(APITestCase):
    
    def setUp(self) -> None:
        shelter = Shelter.objects.create(
            id=100, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        Pet.objects.create(
            id=1, name='São bernardo', age='2 anos', size='grande', shelter=shelter, characteristics='Divertido e elétrico'
        )
        Pet.objects.create(
            id=2, name='pet exemple', age='1 ano', size='pequeno', shelter=shelter, characteristics='Divertido e calmo'
        )

    def test_pet_delete_status_204(self):
        """O Status code retornado, quando for enviada uma requisição delete, deve ser 204"""
        response = self.client.delete('/pets/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_pet_delete_in_data_base(self):
        """O recurso requisitado (delete) deve ser realmente removido do banco de dados"""
        self.client.delete('/pets/2/')
        pet_deleted = Pet.objects.filter(name='pet exemple').exists()
        self.assertFalse(pet_deleted)
    