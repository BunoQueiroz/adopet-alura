from rest_framework.test import APITestCase
from shelter.models import Shelter
from tutor.models import Tutor
from rest_framework import status

class AuthShelterAndTutorTokenTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create_user(
            name='abrigo token',
            city='Paraipaba',
            state='CE',
            username='abrigo-token',
            password='abrigo-token',
            email='email@hotmail.com'
        )
        Tutor.objects.create_user(
            full_name='tutor token',
            username='tutor-token',
            email='emailqualquer@gmail.com',
            password='tutor-token',   
        )
        self.tutor_data = {'username': 'tutor-token', 'password': 'tutor-token'}
        self.shelter_data = {'username': 'abrigo-token', 'password': 'abrigo-token'}

    def test_config_authtoken_shelter(self):
        """Os abrigos devem conseguir autenticação via token"""
        response = self.client.post('/auth/', self.shelter_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_config_authtoken_tutor(self):
        """Os tutores devem conseguir autenticação via token"""
        response = self.client.post('/auth/', self.tutor_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


