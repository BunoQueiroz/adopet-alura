from rest_framework.test import APITestCase
from core.serializers import APIUserSerializer


class APIUserTypeValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.api_user_type_blank = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha0001',
            'confirm_password': 'Senha0001',
            'company_or_user': 'Sou eu de novo',
            'type': '',
        })
        self.api_user_type_capital_letters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha0001',
            'confirm_password': 'Senha0001',
            'company_or_user': 'Sou eu de novo',
            'type': 'M',
        })
        self.api_user_type_two_or_more_letters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha0001',
            'confirm_password': 'Senha0001',
            'company_or_user': 'Sou eu de novo',
            'type': 'fm',
        })
        self.api_user_type_numbers = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha0001',
            'confirm_password': 'Senha0001',
            'company_or_user': 'Sou eu de novo',
            'type': '1',
        })
        self.api_user_type_special_characters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha0001',
            'confirm_password': 'Senha0001',
            'company_or_user': 'Sou eu de novo',
            'type': '@',
        })

    def test_api_user_type_blank(self):
        """Os types de api-user não podem ficar em branco"""
        self.assertFalse(self.api_user_type_blank.is_valid())

    def test_api_user_type_capital_letters(self):
        """Os types de api-user não podem ficar com letras maiúsculas"""
        self.assertFalse(self.api_user_type_capital_letters.is_valid())

    def test_api_user_type_two_or_more_letters(self):
        """Os types de api-user não podem ter mais de uma letra"""
        self.assertFalse(self.api_user_type_two_or_more_letters.is_valid())

    def test_api_user_type_numbers(self):
        """Os types de api-user não podem ser preenchidos com números"""
        self.assertFalse(self.api_user_type_numbers.is_valid())

    def test_api_user_type_special_characters(self):
        """Os types de api-user não podem ser preenchidos com caracteres especiais"""
        self.assertFalse(self.api_user_type_special_characters.is_valid())
