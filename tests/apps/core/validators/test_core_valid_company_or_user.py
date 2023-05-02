from rest_framework.test import APITestCase
from core.serializers import APIUserSerializer


class APIUserCompanyOrUserValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.api_user_company_or_user_small = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': 'eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_special_characters = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': 'c#mp@n! & c!@',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_with_hyphen = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': 'company-usuario',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_with_graphic_accents = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': 'Usuário Número Três',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_only_numbers = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': '12345',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_with_number_and_tree_letters = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': '123pet',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_company_or_user_with_number_and_two_letters = APIUserSerializer(data={
            'email': 'email@valido.com',
            'company_or_user': '123ce',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })

    def test_api_user_company_or_user_small(self):
        """O nome de usuário de (api-user) deve conter ao menos 3 caracteres"""
        self.assertFalse(self.api_user_company_or_user_small.is_valid())

    def test_api_user_company_or_user_with_special_characters(self):
        """Não são permitidos caracteres especiais nos nome de usuário de (api-user). Excessão: ífen (-)"""
        self.assertFalse(self.api_user_company_or_user_special_characters.is_valid())
        self.assertTrue(self.api_user_company_or_user_with_hyphen.is_valid())

    def test_api_user_company_or_user_with_graphic_accents(self):
        """É permitido a utilização de acentos gráficos nos nomes de usuário de (api-user)"""
        self.assertTrue(self.api_user_company_or_user_with_graphic_accents.is_valid())

    def test_api_user_company_or_user_only_numbers(self):
        """Não é permitido que nos nomes de usuário de (api-user) contenha apenas números"""
        self.assertFalse(self.api_user_company_or_user_only_numbers.is_valid())

    def test_api_user_company_or_user_with_numbers_and_at_least_tree_letters(self):
        """Podem haver números nos nomes de usuários de (api-user), contando que haja pelo menos 3 letras sequentes"""
        self.assertFalse(self.api_user_company_or_user_with_number_and_two_letters.is_valid())
        self.assertTrue(self.api_user_company_or_user_with_number_and_tree_letters.is_valid())

