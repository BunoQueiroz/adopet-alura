from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterGETRequestTestCase(APITestCase):
    def setUp(self) -> None:
        self.shelter_paraipaba = Shelter.objects.create(
            id=1,
            name='Abrigo Um',
            road='Rua João Naciso de Oliveira',
            number='03',
            borhood='Pedrinhas',
            CEP='62685-000',
            city='Paraipaba',
            state='CE',
        )

    def test_get_all_shelters(self):
        """Verifica o status 200 sendo devolvidos como resposta"""
        response = self.client.get('/shelters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_shelters_json_format(self):
        """O formato a ser devovlido deve ser JSON"""
        response = self.client.get('/shelters/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_shelter_for_id(self):
        """Os abrigos devem ser disponibilizados de acordo com seu ID"""
        response = self.client.get('/shelters/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_shelter_for_id_in_json_format(self):
        """O formato a ser devovlido deve ser JSON"""
        response = self.client.get('/shelters/1/')
        self.assertEqual(response['Content-Type'], 'application/json')
