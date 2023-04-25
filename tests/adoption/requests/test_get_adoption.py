from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet, Adoption
from tutor.models import Tutor
from rest_framework import status

class AdoptionGETRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        shelter = Shelter.objects.create(id=1, name='Meu abrigo', city='Paraipaba', state='CE')
        pet = Pet.objects.create(id=1, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        tutor = Tutor.objects.create(id=1, full_name='Bruno castro', email='email@gmail.com', password='senha1234')
        Adoption.objects.create(id=1, tutor=tutor, pet=pet, date='2023-05-02')
        
    def test_adoption_get_all_by_anonymou_users_status_401(self):
        """O metodo GET deve retornar status 401 quando todas as adoções forem requisitadas por usuários anônimos"""
        response = self.client.get('/adoptions/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_adoption_get_all_format_JSON(self):
        """O formato retornado às requisições GET no recurso de adoção deve ser JSON"""
        response = self.client.get('/adoptions/')
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_adoption_get_by_id_by_anonymou_users_status_401(self):
        """O metodo GET deve retornar status 401 quando uma adoção por id for requisitada por usuários anônimos"""
        response = self.client.get('/adoptions/1/')
        self.assertTrue(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_adoption_get_by_id_format_JSON(self):
        """O formato retornado às requisições GET no recurso de adoção, em um id específico, deve ser JSON"""
        response = self.client.get('/adoptions/1/')
        self.assertEqual(response['Content-Type'], 'application/json')
        