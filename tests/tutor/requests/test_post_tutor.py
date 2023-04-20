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

    def test_post_tutor_by_anonymous_users_status_401(self):
        """Requisições POST, feita por usuários anônimos, deve retornar status 401"""
        request = self.client.post('/tutors/', self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_tutor_by_anonimous_users_in_data_base(self):
        """Usuários anônimos não devem conseguir inserir novos tutores no banco de dados"""
        self.client.post('/tutors/', self.data)
        new_tutor_expected = Tutor.objects.filter(email='new-email@email.com').exists()
        self.assertFalse(new_tutor_expected)
