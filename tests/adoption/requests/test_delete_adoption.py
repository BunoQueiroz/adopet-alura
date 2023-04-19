from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet, Adoption
from tutor.models import Tutor
from rest_framework import status

class AdoptionDELETERequestsTestCase(APITestCase):

    def setUp(self) -> None:
        shelter = Shelter.objects.create(id=1, name='Meu abrigo', city='Paraipaba', state='CE')
        pet = Pet.objects.create(id=1, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        tutor = Tutor.objects.create(id=1, full_name='Bruno castro', email='email@gmail.com', password='senha1234')
        Adoption.objects.create(id=1, pet=pet, tutor=tutor, date='2023-05-02')
        
    def test_adoption_delete_status_401(self):
        """O status code, ao requisitar um recurso de adoção via DELETE, deve ser 401""" # não autorizado
        response = self.client.delete('/adoptions/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_adoption_delete_in_data_base(self):
        """Uma adoção não pode ser deletada no banco de dados por usuários anônimos"""
        self.client.delete('/adoptions/1/')
        adoption = Adoption.objects.filter(date='2023-05-02').exists()
        self.assertTrue(adoption)
