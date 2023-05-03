from django.urls import reverse
from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet, Adoption
from tutor.models import Tutor
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token


class AdoptionPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        shelter = Shelter.objects.create(id=1, name='Meu abrigo', city='Paraipaba', state='CE')
        Pet.objects.create(id=1, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        Tutor.objects.create(id=1, full_name='Bruno castro', email='email@gmail.com', password='senha1234')
        self.data_status_401 = {'pet': 1, 'tutor': 1, 'date': '2023-05-02'}
        self.data_in_db = {'pet': 1, 'tutor': 1, 'date': '2023-05-03'}

    def test_adoption_post_by_anonymou_user_status_401(self):
        """O status code, para requisições POST de usuários anônimos, deve ser 401"""
        response = self.client.post('/adoptions/', self.data_status_401)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_adoption_post_created_by_anonymou_user_in_data_base(self):
        """Uma adoção, mesmo válida, não deve ser inserida, de fato, no banco de dados por usuários anônimos"""
        self.client.post('/adoptions/', self.data_in_db)
        adoption = Adoption.objects.filter(date='2023-05-03').exists()
        self.assertFalse(adoption)


class AdoptionPOSTRequestsAutorizedTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor = Tutor.objects.create_user('tutoradocao', 'email@tutor.com', 'senha001', id=102, full_name='meu nome')
        self.token = Token.objects.create(user=self.tutor)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token.key}')
        self.url = reverse('adoptions-list')
        shelter = Shelter.objects.create_user('shelter', 'abrigo@tal.com', 'Senha001', id=102, name='Meu abrigo', city='Paraipaba', state='CE')
        Pet.objects.create(id=102, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        self.data_pet_adopted = {'pet': 102, 'tutor': 102, 'date': '2023-05-05'}

    def test_adoption_post_pet_adopted(self):
        """Os pets adotados devem possuir o valor TRUE em seu campo de adoção"""
        self.client.post(self.url, self.data_pet_adopted)
        pet_adopted = get_object_or_404(Pet, pk=102)
        self.assertTrue(pet_adopted.adopted)
