from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse


class AllTutorsDELETERequestsTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_deleted = Tutor.objects.create_user(
            'test delete', 'delete@email.com', 'testdelete01', full_name='test delete', pk=1,
        )
        self.url = reverse('all-tutors')

    def test_all_tutors_delete_by_anonymous_users_status_404(self):
        """O status retornado, ao ser realizada uma requisição DELETE por um usuário anônimo ao recurso de perfil de tutor, deve ser 404"""
        response = self.client.delete(f'{self.url}{self.tutor_deleted.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_all_tutors_delete_by_anonymous_users_data_base(self):
        """Usuários anônimos não deve conseguir DELETAR qualquer usuário tutor por ID"""
        self.client.delete(f'{self.url}{self.tutor_deleted.pk}/')
        pk = self.tutor_deleted.pk
        self.assertTrue(Tutor.objects.filter(pk=pk).exists())


class AllTutorsDELETERequestsTutorAuthorizedTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_authenticated = Tutor.objects.create_user(
            'tutor', 'tutor@gmail.com', 'tutor', full_name='tutor autenticado'
        )
        self.token = Token.objects.create(user=self.tutor_authenticated)
        self.client.credentials(HTTP_AUTHORIZATION=f'token {self.token}')
        self.url = reverse('all-tutors')

    def test_all_tutors_delete_by_tutor_authenticated_outher_tutor_status_404(self):
        """O status retornado, ao ser realizada uma requisição DELETE feita por um tutor autenticado, deve ser 404"""
        response = self.client.delete(f'{self.url}{self.tutor_authenticated.pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_all_tutors_delete_by_tutor_authenticated_in_data_base(self):
        """Tutores autenticados não devem conseguir DELETAR qualquer tutor por id"""
        self.client.delete(f'{self.url}{self.tutor_authenticated.pk}/')
        pk = self.tutor_authenticated.pk
        self.assertTrue(Tutor.objects.filter(pk=pk).exists())
