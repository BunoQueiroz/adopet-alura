from rest_framework.test import APITestCase
from core.serializers import APIUserSerializer


class APIUserPasswordValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.api_user_password_blank = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': '',
            'type': 'm',
            'confirm_password': '',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_up_to_7_characters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'senha00',
            'confirm_password': 'senha00',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_numbers = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': '123456789',
            'confirm_password': '123456789',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_small_letters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'senhacomapenasletras',
            'confirm_password': 'senhacomapenasletras',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_capital_letters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'SENHAMAIUSCULA',
            'confirm_password': 'SENHAMAIUSCULA',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_capital_and_small_letters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'MaiusculaEMinuscula',
            'confirm_password': 'MaiusculaEMinuscula',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_capital_letters_and_numbers = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'SENHA0001',
            'confirm_password': 'SENHA0001',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_only_small_letters_and_numbers = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'senha0001',
            'confirm_password': 'senha0001',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_password_special_characters = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'Senha-deve+ser-Valid0',
            'confirm_password': 'Senha-deve+ser-Valid0',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })
        self.api_user_different_passwords = APIUserSerializer(data={
            'email': 'email@gmail.com',
            'password': 'SenhaValid0',
            'confirm_password': 'SenhaValid01',
            'type': 'm',
            'company_or_user': 'usuário qualquer',
        })

    def test_api_user_password_blank(self):
        """Senhas em branco para os api-users devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_blank.is_valid())

    def test_api_user_password_up_to_7_characters(self):
        """Senhas de api-users com menos de 8 caracteres devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_up_to_7_characters.is_valid())

    def test_api_user_password_only_numbers(self):
        """Senhas de api-users com apenas números devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_only_numbers.is_valid())

    def test_api_user_password_only_letters(self):
        """Senhas de api-users com apenas letras minúsculas ou maiúsculas devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_only_small_letters.is_valid())
        self.assertFalse(self.api_user_password_only_capital_letters.is_valid())

    def test_api_user_password_only_capital_and_small_letters(self):
        """Senhas de api-users com apenas letras maiúsculas e minúsculas devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_only_capital_and_small_letters.is_valid())

    def test_api_user_password_only_capital_small_letters_and_numbers(self):
        """Senhas de api-users com apenas letras minúsculas e números devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_only_capital_letters_and_numbers.is_valid())

    def test_api_user_password_only_capital_letters_and_numbers(self):
        """Senhas de api-users com apenas letras maiúsculas e números devem ser consideradas inválidas"""
        self.assertFalse(self.api_user_password_only_small_letters_and_numbers.is_valid())

    def test_api_user_password_only_special_characters(self):
        """Senhas de api-users com caracteres especiais devem ser consideradas válidas"""
        self.assertTrue(self.api_user_password_special_characters.is_valid())

    def test_api_user_different_passwords(self):
        """A confirmação de senha de api-users deve ser igual à senha 'principal'"""
        self.assertFalse(self.api_user_different_passwords.is_valid())
