from rest_framework.test import APITestCase
from pet.serializers import PetSerializer
from shelter.models import Shelter

class PetCharacteristicsValidTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create(
            id=10, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        self.shelter = Shelter.objects.get(pk=10)
        self.pet_number_in_characteristics = PetSerializer(data={
            'name': 'João Otávio',
            'age': '1 mês',
            'size': 'médio',
            'characteristics': '2eletrico',
            'shelter': self.shelter.pk,
        })
        self.pet_graphic_accents_in_characteristics = PetSerializer(data={
            'name': 'João Otávio',
            'age': '1 mês',
            'size': 'médio',
            'characteristics': 'Életrico',
            'shelter': self.shelter.pk,
        })
        self.pet_two_or_more_characteristics = PetSerializer(data={
            'name': 'João Otávio',
            'age': '1 mês',
            'size': 'médio',
            'characteristics': 'Életrico e Brincalhão',
            'shelter': self.shelter.pk,
        })
        self.pet_special_characters_in_characteristics = PetSerializer(data={
            'name': 'João Otávio',
            'age': '1 mês',
            'size': 'médio',
            'characteristics': '#letrico & Brincalh@o',
            'shelter': self.shelter.pk,
        })
        
    def test_pet_number_in_characteristics(self):
        """Não podem, em hipótese alguma, números nas características dos pets"""
        self.assertFalse(self.pet_number_in_characteristics.is_valid())

    def test_pet_graphic_accents_in_characteristics(self):
        """Podem conter acentuações gráficas nas características dos pets"""
        self.assertTrue(self.pet_graphic_accents_in_characteristics.is_valid())
    
    def test_pet_two_or_more_characteristics(self):
        """Podem haver mais de uma única característica nos pets"""
        self.assertTrue(self.pet_two_or_more_characteristics.is_valid())
    
    def test_pet_special_characters_in_characteristics(self):
        """Podem haver mais de uma única característica nos pets"""
        self.assertFalse(self.pet_special_characters_in_characteristics.is_valid())
