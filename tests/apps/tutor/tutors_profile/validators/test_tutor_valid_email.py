from rest_framework.test import APITestCase
from tutor.serializers import TutorSerializer
from tutor.models import Tutor

class TutorEmailValidTestCase(APITestCase):
    
    def setUp(self):
        self.tutor_with_registered_email = Tutor.objects.create_user(
            username = 'tutor test',
            full_name = 'tutor test',
            email = 'bqueiroz@gmail.com',
            password = 'Password01'
        )
        self.tutor_repeated_email = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz@gmail.com',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_hostless_email = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'email@',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_email_with_only_number = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': '12345@gmail.com',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_email_with_invalid_host = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bruno@132.com',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_email_valid_one = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz048@gmail.com',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_email_valid_two = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz048@gmail.com.br',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })
        self.tutor_email_valid_tree = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz-048@w3school.com.br',
            'password': 'Password01',
            'confirm_password': 'Password01'
        })

    def test_tutor_email_valid(self):
        """Todos os emails deste teste devem ser considerados válidos"""
        self.assertTrue(self.tutor_email_valid_one.is_valid())
        self.assertTrue(self.tutor_email_valid_two.is_valid())
        self.assertTrue(self.tutor_email_valid_tree.is_valid())

    def test_tutor_email_with_only_number(self):
        """Um email que se inicia com números é considerado válido"""
        self.assertFalse(self.tutor_email_with_only_number.is_valid())

    def test_tutor_email_with_invalid_host(self):
        """Um email com host apenas numérico é considerado inválido"""
        self.assertFalse(self.tutor_email_with_invalid_host.is_valid())

    def test_tutor_hostless_email(self):
        """Um email sem host não deve ser considerado válido"""
        self.assertFalse(self.tutor_hostless_email.is_valid())

    def test_tutor_registered_email(self):
        """Emails já cadastrados devem ser considerado inválidos"""
        self.assertFalse(self.tutor_repeated_email.is_valid())
