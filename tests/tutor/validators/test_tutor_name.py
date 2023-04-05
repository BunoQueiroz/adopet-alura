from django.test import TestCase
from tutor.serializers import TutorSerializer

class TutorNameValidTestCase(TestCase):
    def setUp(self):
        self.tutor_unique_name = TutorSerializer(data={
            'full_name': 'test',
            'email': 'email@email.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_name_with_number = TutorSerializer(data={
            'full_name': 'test1 twoortree',
            'email': 'email@email.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })
        self.tutor_name_valid = TutorSerializer(data={
            'full_name': 'Bruno de Castro João Cícero Uchôa',
            'email': 'email@email.com',
            'password': 'password01',
            'confirm_password': 'password01'
        })

    def test_just_name(self):
        """Verifica se apenas nome dos tutores não são válidos"""
        self.assertFalse(self.tutor_unique_name.is_valid())

    def test_with_number(self):
        """Verifica se os nome dos tutores com números não são válidos"""
        self.assertFalse(self.tutor_name_with_number.is_valid())

    def test_fullname_valid(self):
        """Verifica se ao usar 'nome e sobrenome' é realmente válido"""
        self.assertTrue(self.tutor_name_valid.is_valid())
