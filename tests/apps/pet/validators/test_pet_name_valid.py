from rest_framework.test import APITestCase
from pet.serializers import PetSerializer
from shelter.models import Shelter


class PetNameValidTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create(
            id=10, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        self.shelter = Shelter.objects.get(pk=10)
        self.pet_name_with_numbers = PetSerializer(data={
            'name': 'Alex02',
            'age': '7 meses',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_name_with_special_characters = PetSerializer(data={
            'name': 'Alex -+*/!@#$%¨&*()_=}{;:.>,<',
            'age': '7 meses',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_name_with_graphics_accents = PetSerializer(data={
            'name': 'João Otávio',
            'age': '7 meses',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_name_short = PetSerializer(data={
            'name': 'a',
            'age': '7 meses',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })

    def test_pet_number_in_name(self):
        """Não podem haver números nos nomes dos pets"""
        self.assertFalse(self.pet_name_with_numbers.is_valid())
    
    def test_pet_special_characters_in_pet_name(self):
        """Não podem haver caracteres especiais nos nomes dos pets"""
        self.assertFalse(self.pet_name_with_special_characters.is_valid())

    def test_pet_graphics_accents_in_pet_name(self):
        """Podem conter acentuações gráficas nos nomes dos pets"""
        self.assertTrue(self.pet_name_with_graphics_accents.is_valid())

    def test_pet_of_short_name(self):
        """Os nomes dos petes devem conter ao menos dois caracteres"""
        self.assertFalse(self.pet_name_short.is_valid())
