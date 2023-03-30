from django.test import TestCase
from tutor.serializers import TutorSerializer

class TutorEmailTestCase(TestCase):
    def setUp(self):
        self.tutor_hostless_email = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'email@',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_email_with_only_number = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': '12345bbruno@gmail.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_email_with_invalid_host = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bruno@132.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_email_valid_one = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz048@gmail.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_email_valid_two = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz048@gmail.com.br',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_email_valid_tree = TutorSerializer(data={
            'full_name': 'Bruno Castro',
            'email': 'bqueiroz-048@w3school.com.br',
            'password': 'password01',
            'confirm_password': 'password01'
        })

    def test_email_valid(self):
        """Verifica se um email válido é definitivamente considerado válido"""
        self.assertTrue(self.tutor_email_valid_one.is_valid())
        self.assertTrue(self.tutor_email_valid_two.is_valid())
        self.assertTrue(self.tutor_email_valid_tree.is_valid())

    def test_email_with_only_number(self):
        """Verifica se um email que se inicia com números é considerado válido"""
        self.assertFalse(self.tutor_email_with_only_number.is_valid())

    def test_email_with_invalid_host(self):
        """Verifica se um email com host apenas numérico é considerado válido"""
        self.assertFalse(self.tutor_email_with_invalid_host.is_valid())

    def test_hostless_email(self):
        """Verifica se um email sem host é considerado válido"""
        self.assertFalse(self.tutor_hostless_email.is_valid())
