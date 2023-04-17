from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status
from django.shortcuts import get_object_or_404

class ShelterPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_to_upload = Shelter.objects.create(id=1, username='email@email.com', name='Shelter', email='email@email.com', state='CE', password='senha002', borhood='Bairro tal', city='Paraipaba')
        self.data_shelter = {
            'id': 1,
            'username': 'novo-email@gmail.com',
            'password': 'novasenha001',
            'name': 'New Shelter',
            'state': 'CE',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'phone': '85981639630',
        }
        self.shelter_updated = Shelter(
            id=1,
            username='novo-email@gmail.com',
            password='novasenha001',
            email='novo-email@gmail.com',
            name='New Shelter',
            state='CE',
            borhood='Bendita',
            city='Paraipaba',
            phone='85981639630'
        )

    def test_status_200_for_put(self):
        """O status code, quando um abrigo for atualizado, deve retornar 200"""
        response = self.client.put('/shelters/1/', self.data_shelter)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_in_data_base(self):
        """Os dados devem serem atualizados no banco de dados na entidade de Abrigo"""
        self.client.put(path='/shelters/1/', data=self.data_shelter)
        obj_shelter = get_object_or_404(Shelter, pk=1)
        self.assertEqual(self.shelter_updated.name , obj_shelter.name)
        self.assertEqual(self.shelter_updated.state , obj_shelter.state)
        self.assertEqual(self.shelter_updated.city , obj_shelter.city)
        self.assertEqual(self.shelter_updated.phone , obj_shelter.phone)
