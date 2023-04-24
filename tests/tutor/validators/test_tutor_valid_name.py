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

    def test_tutor_just_name(self):
        """Tutores com apenas um nome não devem ser considerado válido"""
        self.assertFalse(self.tutor_unique_name.is_valid())

    def test_tutor_with_number(self):
        """Não deve haver número algum em nomes de tutores"""
        self.assertFalse(self.tutor_name_with_number.is_valid())

    def test_tutor_fullname_valid(self):
        """O exemplo de nome completo deste teste deve ser considerado válido"""
        self.assertTrue(self.tutor_name_valid.is_valid())
