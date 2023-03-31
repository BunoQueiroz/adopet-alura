from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status

class GETRequestsTestCase(APITestCase):
    def setUp(self):
        self.fields_data_tutor_one = {
            'id': 1,
            'full_name': 'tutor test',
            'email': 'email@email.com',
            'password': 'password01',
        }
        self.tutor_one = Tutor.objects.create_user('tutor test', 'email@email.com', 'password01', full_name='tutor test', pk=1)
        
    def test_request_get_all_tutors_return_status_200(self):
        """Verifica se as requisições para pegar todos os tutores está retornando STATUS 200"""
        request = self.client.get('/tutors/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_render_data_all_tutors(self):
        """Verifica se todos os tutores estão sendo devolvidos como resposta"""
        request = self.client.get('/tutors/')
        self.assertEqual(request['Content-Type'], 'application/json')

    def test_request_get_tutors_for_id(self):
        """Verifica se as requisições para pegar tutores por ID está retornando STATUS 200"""
        request = self.client.get('/tutors/1/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
    
    def test_render_data_tutor_especific(self):
        """Verifica se o campos JSON renderizado coincide com os desejado (ID, FULL_NAME, EMAIL, PASSWORD)"""
        request = self.client.get('/tutors/1/')
        self.assertEqual(set(request.json()), set(self.fields_data_tutor_one))
        self.assertEqual(request['Content-Type'], 'application/json')

