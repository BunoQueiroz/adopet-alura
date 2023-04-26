from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterDELETERequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_status_code_deleted = Shelter.objects.create(id=99, name='Novo Abrigo', email='email@gmail.com', username='pemail@gmail.com', password='senhas001', state='CE', borhood='Bendita', city='Paraipaba')
        self.shelter_to_be_deleted = Shelter.objects.create(id=100, name='Novo Abrigo', email='outher-email@gmail.com', username='semail@gmail.com', password='senhas001', state='CE', borhood='Bendita', city='Paraipaba')

    def test_shelter_delete_by_anonymous_users_status_401(self):
        """O status, quando ocorrer uma requisição DELETE de um usuário anônimo, deve ser 401"""
        response = self.client.delete('/shelters/99/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_shelter_delete_by_anonymous_users_in_data_base(self):
        """O abrigo não deve ser deletado, de fato, no banco de dados, por um usuário anônimo"""
        self.client.delete('/shelters/100/')
        shelter_requested = Shelter.objects.filter(pk=100).exists()
        self.assertTrue(shelter_requested)
