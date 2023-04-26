from rest_framework.test import APITestCase
from pet.models import Pet
from shelter.models import Shelter
from tutor.models import Tutor


class PaginationResoursesTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create_user('abrigo@gmail.com', 'abrigo@gmail.com', 'senhas001', name='Abrigo Paraipaba', state='CE', city='Paraipaba')
        self.shelter = Shelter.objects.get(username='abrigo@gmail.com')

    def test_config_pagination_by_pets(self):
        """O recurso de pets deve ter paginação de 10 pets/página por padrão"""
        self.pets_generator()
        response = self.client.get('/pets/')
        self.assertEqual(response.json()['next'], 'http://testserver/pets/?limit=10&offset=10')
        self.assertIsNone(response.json()['previous'])

    def test_config_pagination_by_shelters(self):
        """O recurso de abrigo deve ter paginação de 10 pets/página por padrão"""
        self.shelters_generator()
        response = self.client.get('/shelters/')
        self.assertEqual(response.json()['next'], 'http://testserver/shelters/?limit=10&offset=10')
        self.assertIsNone(response.json()['previous'])

    def test_config_pagination_by_tutors(self):
        """O recurso de tutores deve ter paginação de 10 pets/página por padrão"""
        self.tutors_generator()
        response = self.client.get('/tutors/')
        self.assertEqual(response.json()['next'], 'http://testserver/tutors/?limit=10&offset=10')
        self.assertIsNone(response.json()['previous'])

    def shelters_generator(self):
        for shelter in range(1, 21):
            Shelter.objects.create_user(f'abrigo{shelter}@gmail.com', f'abrigo{shelter}@gmail.com', 'senhas001', name='Abrigo Paraipaba', state='CE', city='Paraipaba')

    def pets_generator(self):
        for pet in range(1, 21):
            Pet.objects.create(name='Pet qualquer', size='medio', age='2 anos', characteristics='Alegre e fiel', shelter=self.shelter)

    def tutors_generator(self):
        for tutor in range(1, 21):
            Tutor.objects.create_user(f'tutor{tutor}', f'em{tutor}@gmail.com', 'senhas001', full_name='tutor tal')

