from rest_framework.test import APITestCase
from shelter.models import Shelter
from pet.models import Pet, Adoption
from tutor.models import Tutor
from rest_framework import status

class AdoptionPOSTRequestsTestCase(APITestCase):

    def setUp(self) -> None:
        shelter = Shelter.objects.create(id=1, name='Meu abrigo', city='Paraipaba', state='CE')
        Pet.objects.create(id=1, name='Meu pet', size='Médio', age='2 meses', shelter=shelter, characteristics='Ágil e fiel')
        Tutor.objects.create(id=1, full_name='Bruno castro', email='email@gmail.com', password='senha1234')
        self.data_status_201 = {'pet': 1, 'tutor': 1, 'date': '2023-05-02'}
        self.data_in_db = {'pet': 1, 'tutor': 1, 'date': '2023-05-03'}

    def test_adoption_post_status_201(self):
        """O status code, ao requisitar via POST no recurso de adoção, deve ser 201"""
        response = self.client.post('/adoptions/', self.data_status_201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_adoption_post_created_in_data_base(self):
        """Uma adoção válida deve ser inserida, de fato, no banco de dados"""
        self.client.post('/adoptions/', self.data_in_db)
        adoption = Adoption.objects.filter(date='2023-05-03').exists()
        self.assertTrue(adoption)
