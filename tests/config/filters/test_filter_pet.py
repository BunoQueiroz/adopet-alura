from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet
from rest_framework import status


class ConfigFilterPetTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter = Shelter.objects.create_user(
            username='abrigoqualquer@gmail.com',
            email='abrigoqualquer@gmail.com',
            password='senhas001',
            name='abrigo qualquer',
            state='CE',
            city='Paraipaba'
        )
        self.pet = Pet.objects.create(
            name='pet principal',
            size='medio',
            age='2 anos',
            characteristics='alegre e fiel',
            shelter=self.shelter
        )
        self.pets_generator()

    def test_config_search_pet_by_full_name(self):
        """Deve ser possível realizar uma pesquisa baseada nos nomes dos petes"""
        response = self.client.get('/pets/?search=pet+principal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_pet_by_size(self):
        """Deve ser possível realizar uma pesquisa baseada nos tamanhos dos petes"""
        response = self.client.get('/pets/?search=medio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_pet_by_age(self):
        """Deve ser possível realizar uma pesquisa baseada nas idades dos petes"""
        response = self.client.get('/pets/?search=2+anos')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_pet_by_characteristics(self):
        """Deve ser possível realizar uma pesquisa baseada nas características dos petes"""
        response = self.client.get('/pets/?search=alegre+e+fiel')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def pets_generator(self):
        for pet in range(5):
            Pet.objects.create(
                name=f'pet{pet}s',
                age=f'1 mês', 
                size='grande', 
                characteristics='feliz e contente',
                shelter=self.shelter
            )

