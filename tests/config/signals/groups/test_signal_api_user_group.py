from django.urls import reverse
from rest_framework.test import APITestCase
from core.models import APIUser


class SignalAPIUserGroupTestCase(APITestCase):

    def setUp(self) -> None:
        self.data = {
            'email': 'email@valido123.com',
            'password': 'Senha001',
            'confirm_password': 'Senha001',
            'type': 'f',
            'company_or_user': 'Bruno'
        }
        self.url = reverse('api-users')

    def test_signals_api_user_belongs_api_user_group(self):
        """Os api-users devem, ao serem criados, pertencer ao seu respectivo grupo"""
        self.client.post(self.url, self.data)
        api_user = APIUser.objects.get(email=self.data['email'])
        group_api_user = api_user.groups.get().name
        self.assertEqual(group_api_user, 'api_user')
    
    def test_signals_api_user_permissions(self):
        """O grupo de api-user deve conter suas devidas permissões"""
        self.client.post(self.url, self.data)
        api_user_groups = APIUser.objects.get(email=self.data['email']).groups.get(name='api_user')
        permissions = ['view_shelter', 'view_pet', 'view_tutor', 'add_tutor', 'add_shelter']
        api_user_permissions = api_user_groups.permissions
        for permission in permissions:
            self.assertTrue(api_user_permissions.filter(codename=permission).exists())
