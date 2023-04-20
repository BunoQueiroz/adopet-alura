from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from pet.models import Pet

class PetPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        current_shelter = Shelter.objects.create(
            id=100, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        new_shelter = Shelter.objects.create(
            id=101, name='Abrigo dois', username='outher-email@email.com', email='outher-email@email.com', city='Paracuru', state='CE',
        )
        Pet.objects.create(
            id=10, name='São bernardo', age='2 anos', size='grande', shelter=current_shelter, characteristics='Divertido e elétrico'
        )
        self.new_data = {
            'name': 'Meu novo nome',
            'age': '3 anos',
            'characteristics': 'Rápido e divertido',
            'size': 'pequeno',
            'shelter': 101,
        }
        self.new_pet = Pet( 
            id=10, name='Meu novo nome', age='3 anos', characteristics='Rápido e divertido', size='pequeno', shelter=new_shelter
        )

    def test_pet_put_status_401(self):
        """O status code retornado, quando um pet for alterado, deve ser 401"""
        response = self.client.put('/pets/10/', self.new_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_pet_put_changed_in_data_base(self):
        """Os pets devem ser alterados, de fato, no banco de dados, caso os dados sejam válidos"""
        self.client.put('/pets/10/', self.new_data)
        changed_pet = Pet.objects.get(pk=10)
        self.assertNotEqual(changed_pet.name, self.new_pet.name)
        self.assertNotEqual(changed_pet.age, self.new_pet.age)
        self.assertNotEqual(changed_pet.characteristics, self.new_pet.characteristics)
        self.assertNotEqual(changed_pet.size, self.new_pet.size)
        self.assertNotEqual(changed_pet.shelter, self.new_pet.shelter)
