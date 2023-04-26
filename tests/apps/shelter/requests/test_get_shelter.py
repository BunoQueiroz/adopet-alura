from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterGETRequestTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_paraipaba = Shelter.objects.create(
            id=1,
            email='email@gmail.com',
            password='senha001',
            name='Abrigo Um',
            borhood='Pedrinhas',
            city='Paraipaba',
            state='CE',
        )

    def test_get_all_shelters_status_200(self):
        """O status 200 deve ser retornado ao ser requisitado, com o verbo get, o recurso de abrigo"""
        response = self.client.get('/shelters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_shelters_json_format(self):
        """Ao serem requisitados, com o verbo get, os recursos de abrigo deve ser renderizado em formato JSON"""
        response = self.client.get('/shelters/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_shelter_by_id(self):
        """Os abrigos devem ser disponibilizados de acordo com seu ID"""
        response = self.client.get('/shelters/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_shelter_by_id_in_json_format(self):
        """Ao sere requisitado, por id, com o verbo get, o recurso de abrigo deve ser renderizado em formato JSON"""
        response = self.client.get('/shelters/1/')
        self.assertEqual(response['Content-Type'], 'application/json')
