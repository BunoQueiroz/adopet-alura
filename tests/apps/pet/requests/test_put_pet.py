from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from pet.models import Pet

class PetPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_shelter = Shelter.objects.create_user('abrigo@gmail.com', 'abrigo@gmail.com', 'shelter', city='Cidade tal', state='CE', name='abrigo mais novo')        
        self.shelter = Shelter.objects.get(email='abrigo@gmail.com')
        self.pet = Pet.objects.create(id=1, name='São bernardo', age='2 anos', size='grande', characteristics='alegre e agil', shelter=self.shelter)
        self.new_pet = Pet(id=10, name='Meu novo nome', age='3 anos', characteristics='Rápido e divertido', size='pequeno', shelter=self.shelter)
        self.new_data = {
            'name': 'Meu novo nome',
            'age': '3 anos',
            'characteristics': 'Rápido e divertido',
            'size': 'pequeno',
            'shelter': self.shelter.pk,
        }

    def test_pet_put_status_401(self):
        """O status code retornado, quando um pet for alterado, deve ser 401"""
        response = self.client.put('/pets/1/', self.new_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_pet_put_changed_in_data_base(self):
        """Os pets não devem ser alterados, de fato, no banco de dados, por usuários anônimos"""
        self.client.put('/pets/1/', self.new_data)
        changed_pet = Pet.objects.get(pk=1)
        self.assertNotEqual(changed_pet.name, self.new_pet.name)
        self.assertNotEqual(changed_pet.age, self.new_pet.age)
        self.assertNotEqual(changed_pet.characteristics, self.new_pet.characteristics)
        self.assertNotEqual(changed_pet.size, self.new_pet.size)
