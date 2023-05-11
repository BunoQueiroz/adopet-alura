from tutor.models import Tutor
from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import get_object_or_404
from django.urls import reverse


class TutorsProfilePUTResquestsTestCase(APITestCase):
    
    def setUp(self):
        self.data = {
            'full_name': 'bruno de castro',
            'email': 'new_email@gmail.com',
            'password': 'senha002',
            'confirm_password': 'Senha002'
        }
        self.tutor_one = Tutor.objects.create_user(
            pk = 1,
            full_name = 'brunos castro',
            username = 'brunos castro',
            email = 'email@gmail.com',
            password = 'senha001'
        )
        self.url = reverse('tutors-list')

    def test_put_tutor_profile_by_anonymous_users_status_404(self):
        """Requisições PUT, realizadas por usuários anônimosa aos perfis de tutores, deve retornar status 404"""
        response = self.client.put(f'{self.url}{self.tutor_one.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_tutor_profile_by_anonymous_users_in_data_base(self):
        """Usuários anônimos não devem conseguir Atualizar o recurso de tutor"""
        self.client.put(f'{self.url}{self.tutor_one.pk}/', self.data)
        obj_tutor = get_object_or_404(Tutor, pk=1)
        self.assertNotEqual(self.data['full_name'] , obj_tutor.full_name)
        self.assertNotEqual(self.data['email'] , obj_tutor.email)
        self.assertNotEqual(self.data['email'] , obj_tutor.username)
