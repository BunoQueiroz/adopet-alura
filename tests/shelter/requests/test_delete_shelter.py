from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterDELETERequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_status_code_deleted = Shelter.objects.create(id=99, name='Novo Abrigo', road='Rua Nova', state='CE', number=3, borhood='Bendita', city='Paraipaba', CEP='65685-000')
        self.shelter_to_be_deleted = Shelter.objects.create(id=100, name='Novo Abrigo', road='Rua Nova', state='CE', number=3, borhood='Bendita', city='Paraipaba', CEP='65685-000')

    def test_delete_shelter_status_204(self):
        """Deve ser retornado um status code de 204 quando um abrigo for deletado"""
        response = self.client.delete('/shelters/99/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_shelter_in_data_base(self):
        """O abrigo deve ser deletado, de fato, no banco de dados"""
        self.client.delete('/shelters/100/')
        shelter_deleted = Shelter.objects.filter(pk=100).exists()
        self.assertFalse(shelter_deleted)
