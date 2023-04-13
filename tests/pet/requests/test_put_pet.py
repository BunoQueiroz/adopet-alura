from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from pet.models import Pet

class PetPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        current_shelter = Shelter.objects.create(
            id=200, name='Abrigo Um', road='Rua João Naciso de Oliveira', number='03', borhood='Pedrinhas', CEP='62685-000', city='Paraipaba', state='CE',
        )
        new_shelter = Shelter.objects.create(
            id=201, name='Abrigo Dois', road='Rua João Naciso Pedro', number='05', borhood='Pedrinhas', CEP='62685-000', city='Paraipaba', state='CE',
        )
        Pet.objects.create(
            id=10, name='São bernardo', age='2 anos', size='grande', shelter=current_shelter, characteristics='Divertido e elétrico'
        )
        self.new_data = {
            'name': 'Meu novo nome',
            'age': '3 anos',
            'characteristics': 'Rápido e divertido',
            'size': 'grande',
            'shelter': 201,
        }
        self.new_pet = Pet( 
            id=10, name='Meu novo nome', age='3 anos', characteristics='Rápido e divertido', size='grande', shelter=new_shelter
        )

    def test_pet_put_status_200(self):
        """O status code retornado, quando um pet for alterado, deve ser 200"""
        response = self.client.put('/pets/10/', self.new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pet_put_changed_in_data_base(self):
        """Os pets devem ser alterados, de fato, no banco de dados, caso os dados sejam válidos"""
        self.client.put('/pets/10/', self.new_data)
        changed_pet = Pet.objects.get(pk=10)
        self.assertEqual(changed_pet, self.new_pet)
