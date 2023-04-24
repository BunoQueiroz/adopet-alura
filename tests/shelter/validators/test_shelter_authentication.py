from shelter.models import Shelter
from rest_framework.test import APITestCase
from django.contrib import auth

class ShelterAuthenticationTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create_user(username='email@gmail.com', password='senha001', name='carlos', state='CE', city='Paraipaba')

    def test_shelter_authentication(self):
        """Os abrigos devem ser autenticados, semelhantemente à um User"""
        shelter_authenticated = auth.authenticate(username='email@gmail.com', password='senha001')
        shelter_not_authenticated = auth.authenticate(username='inexists-email@gmail.com', password='senha001')
        self.assertIsNotNone(shelter_authenticated)
        self.assertIsNone(shelter_not_authenticated)
