from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status

class DELETERequestsTestCase(APITestCase):
    def setUp(self):
        self.tutor_one = Tutor.objects.create_user('test delete', 'delete@email.com', 'testdelete01', full_name='test delete', pk=1)
        self.tutor_two = Tutor.objects.create_user('more test delete', 'moredelete@email.com', 'testdelete01', full_name='more test delete', pk=2)

    def test_delete_tutor_for_id(self):
        """Verifica se as requisições DELETE por ID estão devolvendo STATUS 204"""
        delete_tutor_one = self.client.delete('/tutors/1/')
        self.assertEqual(delete_tutor_one.status_code, status.HTTP_204_NO_CONTENT)
        delete_tutor_two = self.client.delete('/tutors/2/')
        self.assertEqual(delete_tutor_two.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tutor_data_base(self):
        """Verifica se os recursos da api que recebem requisição DELETE estão sendo excluídos do banco de dados"""
        self.client.delete('/tutors/1/')
        self.client.delete('/tutors/2/')
        self.assertFalse(Tutor.objects.filter(pk=1).exists())
        self.assertFalse(Tutor.objects.filter(pk=2).exists())
