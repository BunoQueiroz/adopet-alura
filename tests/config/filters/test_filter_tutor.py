from rest_framework.test import APITestCase
from tutor.models import Tutor
from rest_framework import status


class ConfigFilterTutorTestCase(APITestCase):

    def setUp(self) -> None:
        self.tutor = Tutor.objects.create_user(
            username='tutorprincipal@gmail.com',
            email='tutorprincipal@gmail.com',
            password='senhas001',
            full_name='tutor principal',
        )
        self.tutors_generator()

    def test_config_search_tutor_by_full_name(self):
        """Deve ser possível realizar uma pesquisa baseada nos nomes dos tutores"""
        response = self.client.get('/tutors/?search=tutor+principal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def test_config_search_tutor_by_email(self):
        """Deve ser possível realizar uma pesquisa baseada nos emails dos tutores"""
        response = self.client.get('/tutors/?search=tutorprincipal@gmail.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)

    def tutors_generator(self):
        for tutor in range(5):
            Tutor.objects.create_user(
                username=f'tutor{tutor}@gmail.com',
                email=f'tutor{tutor}@gmail.com', 
                password='senhas001', 
                full_name='tutores secundários',
            )
