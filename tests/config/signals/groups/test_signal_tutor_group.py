from django.contrib.auth.models import User
from tutor.models import Tutor
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class SignalsTutorGroupTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser('bruno', 'bruno@gmail.com', 'senha001')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.data = {
            'full_name': 'Bruno de Castro',
            'email': 'bqueiroz@gmail.com',
            'password': 'senha001',
            'confirm_password': 'senha001',
        }

    def test_signals_tutor_belongs_tutor_group(self):
        """Quando um tutor for criado, ele deve pertencer à um grupo chamado 'tutor'"""
        self.client.post('/tutors/', self.data)
        tutor = Tutor.objects.get(username='bqueiroz@gmail.com')
        self.assertEqual(tutor.groups.get().name, 'tutor')

    def test_signals_tutor_group_permissions(self):
        """Os tutores possuem as permissões de usuário anônimo e permissões sobre o recurso de tutores"""
        self.client.post('/tutors/', self.data)
        tutor = Tutor.objects.get(username='bqueiroz@gmail.com')
        permissions = ['view_pet', 'view_tutor', 'view_shelter', 'add_tutor', 'change_tutor', 'delete_tutor']
        tutor_permissions = tutor.groups.get().permissions
        for permission in permissions:
            self.assertTrue(tutor_permissions.filter(codename=permission).exists())
