from tutor.models import Tutor
from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import get_object_or_404

class TutorPUTResquestsTestCase(APITestCase):
    
    def setUp(self):
        self.data = {
            'full_name': 'bruno de castro',
            'email': 'new_email@gmail.com',
            'password': 'senha002',
            'confirm_password': 'senha002'
        }
        self.tutor_one = Tutor.objects.create_user(
            pk = 1,
            full_name = 'brunos castro',
            username = 'brunos castro',
            email = 'email@gmail.com',
            password = 'senha001'
        )

    def test_put_tutor_by_anonymous_users_status_401(self):
        """Requisições PUT, realizadas por usuários anônimos, deve retornar status 401"""
        request = self.client.put(path='/tutors/1/', data=self.data)
        self.assertEqual(request.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_tutor_by_anonymous_users_in_data_base(self):
        """Usuários anônimos não devem conseguir Atualizar o recurso de tutor"""
        self.client.put(path='/tutors/1/', data=self.data)
        obj_tutor = get_object_or_404(Tutor, pk=1)
        self.assertNotEqual(self.data['full_name'] , obj_tutor.full_name)
        self.assertNotEqual(self.data['email'] , obj_tutor.email)
        self.assertNotEqual(self.data['email'] , obj_tutor.username)
