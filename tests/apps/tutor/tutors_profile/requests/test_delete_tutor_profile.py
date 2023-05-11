from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse


class TutorsProfileDELETERequestsTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_one = Tutor.objects.create_user('test delete', 'delete@email.com', 'testdelete01', full_name='test delete', pk=1)
        self.url = reverse('tutors-list')

    def test_tutor_delete_by_anonymous_users_by_id(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um usuário anônimo, deve ser 404"""
        response = self.client.delete(f'{self.url}{self.tutor_one.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_tutor_delete_by_anonymous_users_data_base(self):
        """Usuários anônimos não deve conseguir DELETAR qualquer tutor por id"""
        self.client.delete(f'{self.url}{self.tutor_one.pk}/')
        self.assertTrue(Tutor.objects.filter(pk=1).exists())


class TutorsProfileDELETERequestsAuthenticatedTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_authenticated = Tutor.objects.create_user(
            'tutor', 'tutor@gmail.com', 'tutor', full_name='tutor autenticado', pk=11
        )
        self.token = Token.objects.create(user=self.tutor_authenticated)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token.key}')
        self.url = reverse('tutors-list')

    def test_tutor_delete_by_tutor_authenticated_by_id(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um tutor autenticado, deve ser 204"""
        response = self.client.delete(f'{self.url}{self.tutor_authenticated.auth_token}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_tutor_delete_by_tutor_authenticated_in_data_base(self):
        """Tutores autenticados deve conseguir DELETAR tutores"""
        self.client.delete(f'{self.url}{self.tutor_authenticated.auth_token}/')
        self.assertFalse(Tutor.objects.filter(pk=11).exists())
