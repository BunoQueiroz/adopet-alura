from tutor.models import Tutor
from rest_framework import status
from rest_framework.test import APITestCase
from django.shortcuts import get_object_or_404

class TutorUpdateTestCase(APITestCase):
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

    def test_verify_put_requests(self):
        """Verifica se as requisições PUT sendo recebidas com sucesso"""
        request = self.client.put(path='/tutors/1/', data=self.data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_successful_change_full_name(self):
        """Verifica se as alterações no NOME COMPLETO estão ocorrendo como esperado no banco de dados"""
        self.client.put(path='/tutors/1/', data=self.data)
        obj_tutor = get_object_or_404(Tutor, pk=1)
        self.assertEqual(self.data['full_name'] , obj_tutor.full_name)

    def test_successful_change_email(self):
        """Verifica se a alteração de EMAIL está ocorrendo como esperado no banco de dados"""
        self.client.put(path='/tutors/1/', data=self.data)
        obj_tutor = get_object_or_404(Tutor, pk=1)
        self.assertEqual(self.data['email'] , obj_tutor.email)
