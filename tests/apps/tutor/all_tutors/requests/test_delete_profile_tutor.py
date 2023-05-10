from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse


class TutorProfileDELETERequestsTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_deleted = Tutor.objects.create_user(
            'test delete', 'delete@email.com', 'testdelete01', full_name='test delete'
        )
        self.url = reverse('tutor-profiles-list')

    def test_profile_tutor_delete_by_anonymous_users(self):
        """O status retornado, ao ser realizada uma requisição DELETE por um usuário anônimo ao recurso de perfil de tutor, deve ser 401"""
        response = self.client.delete(f'{self.url}{self.tutor_deleted.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_profile_tutor_delete_by_anonymous_users_data_base(self):
        """Usuários anônimos não deve conseguir DELETAR qualquer perfil de tutor"""
        self.client.delete(f'{self.url}{self.tutor_deleted.pk}/')
        pk = self.tutor_deleted.pk
        self.assertTrue(Tutor.objects.filter(pk=pk).exists())


class TutorProfileDELETERequestsTutorAuthorizedTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_authenticated = Tutor.objects.create_user(
            'tutor', 'tutor@gmail.com', 'tutor', full_name='tutor autenticado'
        )
        self.token = Token.objects.create(user=self.tutor_authenticated)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.url = reverse('tutor-profiles-list')

    def test_profile_tutor_delete_by_tutor_authenticated_your_profile(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um tutor autenticado, deve ser 204"""
        response = self.client.delete(f'{self.url}{self.tutor_authenticated.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_profile_tutor_delete_by_tutor_authenticated_in_data_base(self):
        """Tutores autenticados deve conseguir DELETAR seu próprio perfil"""
        self.client.delete(f'{self.url}{self.tutor_authenticated.pk}/')
        pk = self.tutor_authenticated.pk
        self.assertFalse(Tutor.objects.filter(pk=pk).exists())
