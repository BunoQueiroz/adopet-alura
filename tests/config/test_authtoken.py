from rest_framework.test import APITestCase
from shelter.models import Shelter
from tutor.models import Tutor
from rest_framework import status
from core.models import APIUser


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
        APIUser.objects.create_user(
            company_or_user='usuario mobile',
            username='apiuser-token',
            email='emailmobile@gmail.com',
            password='Senha001',   
        )
        self.tutor_data = {'username': 'tutor-token', 'password': 'tutor-token'}
        self.shelter_data = {'username': 'abrigo-token', 'password': 'abrigo-token'}
        self.api_user_data = {'username': 'apiuser-token', 'password': 'Senha001'}

    def test_config_authtoken_shelter(self):
        """Os abrigos devem conseguir autenticação via token"""
        response = self.client.post('/auth/', self.shelter_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_config_authtoken_tutor(self):
        """Os tutores devem conseguir autenticação via token"""
        response = self.client.post('/auth/', self.tutor_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_config_authtoken_api_user(self):
        """Os 'usuários externos' devem conseguir autenticação via token"""
        response = self.client.post('/auth/', self.api_user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
