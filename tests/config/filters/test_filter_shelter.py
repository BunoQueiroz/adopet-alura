from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status


class ConfigFilterShelterTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter = Shelter.objects.create_user(
            username='abrigoprincipal@gmail.com',
            email='abrigoprincipal@gmail.com',
            password='senhas001',
            name='abrigo principal',
            state='SP',
            city='São Paulo'
        )
        self.shelters_generator()

    def test_config_search_shelter_by_name(self):
        """Deve ser possível realizar uma pesquisa baseada nos nomes dos abrigos"""
        response = self.client.get('/shelters/?search=abrigo+principal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_shelter_by_email(self):
        """Deve ser possível realizar uma pesquisa baseada nos emails dos abrigos"""
        response = self.client.get('/shelters/?search=abrigoprincipal@gmail.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_shelter_by_state(self):
        """Deve ser possível realizar uma pesquisa baseada nos estados dos abrigos"""
        response = self.client.get('/shelters/?search=SP')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_shelter_by_city(self):
        """Deve ser possível realizar uma pesquisa baseada nas cidades dos abrigos"""
        response = self.client.get('/shelters/?search=São+Paulo')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def shelters_generator(self):
        for shelter in range(5):
            Shelter.objects.create_user(
                username=f'abri{shelter}go@gmail.com',
                email=f'abri{shelter}go@gmail.com', 
                password='senhas001', 
                name='abrigos secundários',
                city='Paraipaba',
                state='CE',
            )
