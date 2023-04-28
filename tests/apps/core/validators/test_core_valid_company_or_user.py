from rest_framework.test import APITestCase
from core.serializers import APIUserSerializer


class APIUserCompanyOrUserValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.api_user_email_blank = APIUserSerializer(data={
            'email': '',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_without_domain = APIUserSerializer(data={
            'email': 'emailtal@',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_only_numbers = APIUserSerializer(data={
            'email': '12345@gmail.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_domain_only_numbers = APIUserSerializer(data={
            'email': 'email@1234.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_incomplete_domain = APIUserSerializer(data={
            'email': 'exemplo@email',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_special_characters = APIUserSerializer(data={
            'email': 'ex&mpl@$@email.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_special_characters_exeption = APIUserSerializer(data={
            'email': 'email-exemplo@gmail.com.br',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_special_characters_in_domain = APIUserSerializer(data={
            'email': 'exemplo@e$#il.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_special_characters_in_domain_exeption = APIUserSerializer(data={
            'email': 'exemplo@domain-exeption.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_valid_one = APIUserSerializer(data={
            'email': 'exemplo@email.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_valid_two = APIUserSerializer(data={
            'email': 'exemplo@w3schools.com',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_valid_tree = APIUserSerializer(data={
            'email': 'exemplo@governo.gov.br',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })
        self.api_user_email_valid_four = APIUserSerializer(data={
            'email': 'mais-exemplo@governo.gov.br',
            'company_or_user': 'sou eu',
            'password': 'Senhas001',
            'confirm_password': 'Senhas001',
            'type': 'a',
        })

    def test_api_user_email_blank(self):
        """O campo de email para o modelo de api-user não pode estar em branco"""
        self.assertFalse(self.api_user_email_blank.is_valid())

    def test_api_user_email_without_domain(self):
        """Os emails de api-user não podem estar sem seu domínio"""
        self.assertFalse(self.api_user_email_without_domain.is_valid())

    def test_api_user_email_with_only_numbers(self):
        """Os emails de api-user não podem ser somente números"""
        self.assertFalse(self.api_user_email_only_numbers.is_valid())

    def test_api_user_email_with_domain_only_numbers(self):
        """Os emails de api-user não podem ter somente números em seus domíneos"""
        self.assertFalse(self.api_user_email_domain_only_numbers.is_valid())

    def test_api_user_email_with_incomplete_domain(self):
        """Os emails de api-user não podem possuir domíneos sem .'alguma-coisa'"""
        self.assertFalse(self.api_user_email_incomplete_domain.is_valid())

    def test_api_user_email_special_characters(self):
        """Os emails de api-user não podem possuir caracteres especiais. Exceção: '-'"""
        self.assertFalse(self.api_user_email_special_characters.is_valid())
        self.assertTrue(self.api_user_email_special_characters_exeption.is_valid())

    def test_api_user_email_special_characters_in_domain(self):
        """Os emails de api-user não podem possuir caracteres especiais em seus domíneos. Exceção: '-'"""
        self.assertFalse(self.api_user_email_special_characters_in_domain.is_valid())
        self.assertTrue(self.api_user_email_special_characters_in_domain_exeption.is_valid())

    def test_api_user_email_valid(self):
        """Os emails deste teste devem ser considerados válidos"""
        self.assertTrue(self.api_user_email_valid_one.is_valid())
        self.assertTrue(self.api_user_email_valid_two.is_valid())
        self.assertTrue(self.api_user_email_valid_tree.is_valid())
        self.assertTrue(self.api_user_email_valid_four.is_valid())
