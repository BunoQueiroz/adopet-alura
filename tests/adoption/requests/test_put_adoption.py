from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet, Adoption
from tutor.models import Tutor
from rest_framework import status

class AdoptionPUTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        shelter = Shelter.objects.create(id=1, name='Meu abrigo', city='Paraipaba', state='CE')
        pet = Pet.objects.create(id=1, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        tutor = Tutor.objects.create(id=1, full_name='Bruno castro', email='email@gmail.com', password='senha1234')
        self.adoption = Adoption.objects.create(id=1, pet=pet, tutor=tutor, date='2023-05-02')
        self.data_in_db = {'pet': 1, 'tutor': 1, 'date': '2023-05-03'}

    def test_adoption_put_status_405(self):
        """O status code, ao requisitar o recurso de adoção via PUT, deve ser 405"""
        response = self.client.put('/adoptions/1/', self.data_in_db)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_adoption_put_created_in_data_base(self):
        """Uma adoção não pode ser alterada, em hipótese alguma, no banco de dados"""
        self.client.put('/adoptions/1/', self.data_in_db)
        adoption = Adoption.objects.filter(date='2023-05-03').exists()
        self.assertFalse(adoption)
