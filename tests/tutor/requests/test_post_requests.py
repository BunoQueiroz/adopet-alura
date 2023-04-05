from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status

class TutorPOSTRequestsTestCase(APITestCase):
    def setUp(self):
        self.data = {
            'full_name': 'tutor test post',
            'email': 'new-email@email.com',
            'password': 'NewPassword01',
            'confirm_password': 'NewPassword01',
        }
        self.tutor_one = Tutor.objects.create_user('test post', 'post@email.com', 'testpost01', full_name='test post', pk=100)

    def test_request_new_tutor_status_200(self):
        """Verifica se a criação de novos tutores devolve STATUS 201"""
        request = self.client.post('/tutors/', self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
    
    def test_new_tutor_created(self):
        """Verifica se a criação de novos tutores está ocorrendo de fato no banco de dados"""
        self.client.post('/tutors/', self.data)
        new_tutor_expected = Tutor.objects.filter(email='new-email@email.com').exists()
        self.assertTrue(new_tutor_expected)
