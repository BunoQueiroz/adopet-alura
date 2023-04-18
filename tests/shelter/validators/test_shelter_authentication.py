from shelter.models import Shelter
from rest_framework.test import APITestCase
from django.contrib import auth
from django.contrib.sessions.backends.db import SessionStore
from rest_framework.request import Request
from django.http import HttpRequest

class ShelterAuthenticationTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create_user(username='email@gmail.com', password='senha001', name='carlos', state='CE', city='Paraipaba')

    def test_shelter_authentication(self):
        """Os abrigos devem ser autenticados, semelhantemente à um User"""
        shelter_authenticated = auth.authenticate(username='email@gmail.com', password='senha001')
        shelter_not_authenticated = auth.authenticate(username='inexists-email@gmail.com', password='senha001')
        self.assertIsNotNone(shelter_authenticated)
        self.assertIsNone(shelter_not_authenticated)

    '''def test_shelter_login(self):
        """Os abrigos devem realizar o login, para possuírem as devidas permissões"""
        http_request = HttpRequest()
        http_request.session = SessionStore()
        request = Request(http_request)
        shelter = auth.authenticate(request, username='email@gmail.com', password='senha001')
        shelter_logged = auth.login(request, shelter)
        self.assertIsNone(shelter_logged)'''

