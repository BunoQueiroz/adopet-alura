from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from shelter.models import Shelter

class SignalsShelterGroupTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser('bruno', '', 'bruno')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.data = {
            'name': 'Abrigo de teste',
            'city': 'cidade qualquer',
            'borhood': '',
            'phone': '',
            'state': 'CE',
            'email': 'emailtest@gmail.com',
            'password': 'senhas001',
        }

    def test_shelter_in_shelter_group(self):
        """Todos os abrigos cadastrados devem pertencer ao seu respectivo grupo"""
        self.client.post('/shelters/', self.data)
        shelter = Shelter.objects.get(email='emailtest@gmail.com')
        self.assertEqual(shelter.groups.get().name, 'shelter')

    def test_permissions_shelter_group(self):
        self.client.post('/shelters/', self.data)
        shelter_group = Shelter.objects.get(email='emailtest@gmail.com').groups.get()
        group_permissions = shelter_group.permissions
        permissions = ['view_shelter', 'view_pet', 'add_pet', 'change_pet', 'delete_pet', 'view_tutor', 'change_shelter', 'add_shelter', 'delete_shelter', 'view_adoption', 'delete_adoption']
        for permission in permissions:
            self.assertTrue(group_permissions.filter(codename=permission).exists())
