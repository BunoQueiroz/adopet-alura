from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer

class ShelterPasswordValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_numeric_email = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': '1234@gmail.com'
        })
        self.shelter_email_with_capital_letters = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': 'EmailCapitalLeters@gmail.com'
        })
        self.shelter_email_with_letters_and_numbers = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': 'email1234@gmail.com'
        })
        self.shelter_email_starting_with_number = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': '88email1234@gmail.com'
        })
        self.shelter_email_starting_with_special_character = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': '#email1234@gmail.com'
        })
        self.shelter_email_without_domain = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': 'email1234@'
        })
        self.shelter_email_with_numeric_domain = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': 'email1234@1234.com'
        })
        self.shelter_email_with_domain_letter_and_number = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': 'email1234@w3schools.com'
        })
        self.shelter_email_blank = ShelterSerializer(data={
            'name': 'abrigo teste',
            'city': 'Paraipaba',
            'state': 'CE',
            'borhood': '',
            'phone': '',
            'password': 'senhas001',
            'confirm_password': 'senhas001',
            'email': ''
        })

    def test_shelter_numeric_email(self):
        """Emails com apenas números devem ser considerados inválidos"""
        self.assertFalse(self.shelter_numeric_email.is_valid())

    def test_shelter_email_with_capital_letters(self):
        """Emails com letras maiúsculas devem ser considerados inválidos"""
        self.assertFalse(self.shelter_email_with_capital_letters.is_valid())

    def test_shelter_email_with_letters_and_numbers(self):
        """Os emails dos abrigo podem conter letras e números"""
        self.assertTrue(self.shelter_email_with_letters_and_numbers.is_valid())
    
    def test_shelter_email_with_letters_and_numbers(self):
        """Os emails dos abrigo devem ser iniciados com letras"""
        self.assertFalse(self.shelter_email_starting_with_number.is_valid())
        self.assertFalse(self.shelter_email_starting_with_special_character.is_valid())
    
    def test_shelter_email_without_domain(self):
        """Os emails dos abrigo não podem ficar sem seus respectivos domínios"""
        self.assertFalse(self.shelter_email_without_domain.is_valid())
    
    def test_shelter_email_with_numeric_domain(self):
        """Os emails dos abrigo não podem conter somente números em seus domínios"""
        self.assertFalse(self.shelter_email_with_numeric_domain.is_valid())
    
    def test_shelter_email_domain_with_letters_and_numbers(self):
        """Os emails dos abrigo podem conter letras e números em seus domínios"""
        self.assertTrue(self.shelter_email_with_domain_letter_and_number.is_valid())
    
    def test_shelter_email_blank(self):
        """Os emails dos abrigo não são opcionais, são obrigatórios"""
        self.assertFalse(self.shelter_email_blank.is_valid())
