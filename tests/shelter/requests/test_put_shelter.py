from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_to_upload = Shelter.objects.create(id=1, name='Shelter', road='Rua tal', state='CE', number=5, borhood='Bairro tal', city='Paraipaba', CEP='65652-000')
        self.data_shelter = {
            'name': 'New Shelter',
            'road': 'Rua Nova',
            'state': 'CE',
            'number': '03',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'CEP': '65685-000',
        }
        self.shelter_updated = Shelter(id=1, name='New Shelter', road='Rua Nova', state='CE', number=3, borhood='Bendita', city='Paraipaba', CEP='65685-000')

    def test_status_200_for_put(self):
        """O status code, quando um abrigo for atualizado, deve retornar 200"""
        response = self.client.put('/shelters/1/', self.data_shelter)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_upload_in_data_base(self):
        """Os dados devem serem atualizados no banco de dados na entidade de Abrigo"""
        self.client.put('/shelters/1/', self.data_shelter)
        shelter_now = Shelter.objects.get(pk=1)
        self.assertEqual(shelter_now, self.shelter_updated)


