from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse


class TutorDELETERequestsTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_one = Tutor.objects.create_user('test delete', 'delete@email.com', 'testdelete01', full_name='test delete', pk=1)
        self.tutor_two = Tutor.objects.create_user('more test delete', 'moredelete@email.com', 'testdelete01', full_name='more test delete', pk=2)

    def test_tutor_delete_by_anonymous_users_by_id(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um usuário anônimo, deve ser 401"""
        delete_tutor_one = self.client.delete('/tutors/1/')
        self.assertEqual(delete_tutor_one.status_code, status.HTTP_401_UNAUTHORIZED)
        delete_tutor_two = self.client.delete('/tutors/2/')
        self.assertEqual(delete_tutor_two.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_tutor_delete_by_anonymous_users_data_base(self):
        """Usuários anônimos não deve conseguir DELETAR qualquer tutor"""
        self.client.delete('/tutors/1/')
        self.client.delete('/tutors/2/')
        self.assertTrue(Tutor.objects.filter(pk=1).exists())
        self.assertTrue(Tutor.objects.filter(pk=2).exists())


class TutorDELETERequestsTutorAuthorizedTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_authenticated = Tutor.objects.create_user('tutor', 'tutor@gmail.com', 'tutor', full_name='tutor autenticado')
        self.token = Token.objects.create(user=self.tutor_authenticated)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token.key}')
        self.tutor_one = Tutor.objects.create_user('test delete', 'delete@email.com', 'testdelete01', full_name='test delete', pk=1)
        self.tutor_two = Tutor.objects.create_user('more test delete', 'moredelete@email.com', 'testdelete01', full_name='more test delete', pk=2)
        self.url = reverse('tutors-list')

    def test_tutor_delete_by_tutor_authenticated_by_id(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um tutor autenticado, deve ser 204"""
        delete_tutor_one = self.client.delete(f'{self.url}{self.tutor_one.pk}/')
        self.assertEqual(delete_tutor_one.status_code, status.HTTP_204_NO_CONTENT)

    def test_tutor_delete_by_tutor_authenticated_in_data_base(self):
        """Tutores autenticados deve conseguir DELETAR tutores"""
        self.client.delete(f'{self.url}{self.tutor_one.pk}/')
        self.client.delete(f'{self.url}{self.tutor_two.pk}/')
        self.assertFalse(Tutor.objects.filter(pk=1).exists())
        self.assertFalse(Tutor.objects.filter(pk=2).exists())
