from rest_framework.test import APITestCase
from shelter.models import Shelter
from rest_framework import status

class ShelterPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        self.data_shelter_post_id_200 = {
            'name': 'Abrigos diferentes',
            'password': 'senhas001',
            'email': 'emails@gmail.com',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        }
        self.data_shelter_post_id_401 = {
            'name': 'Abrigo diferente',
            'password': 'senhas001',
            'email': 'emails@gmail.com',
            'borhood': 'Bendita',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '',
        }
    
    def test_shelter_post_by_anonymous_users_status_401(self):
        """O Status retornado, para usuários anônimos, deve ser 401"""
        response = self.client.post('/shelters/', self.data_shelter_post_id_401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_shelter_post_by_anonymous_users_in_data_base(self):
        """Usuários anônimos não devem conseguir alterar dados no banco de dados"""
        self.client.post('/shelters/', self.data_shelter_post_id_200)
        shelter_exists = Shelter.objects.filter(name='Abrigos diferentes').exists()
        self.assertFalse(shelter_exists)
