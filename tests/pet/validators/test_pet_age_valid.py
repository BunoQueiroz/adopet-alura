from rest_framework.test import APITestCase
from pet.serializers import PetSerializer
from shelter.models import Shelter

class PetAgeValidTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create(
            id=10, name='Abrigo Um', road='Rua João Naciso de Oliveira', number='03', borhood='Pedrinhas', CEP='62685-000', city='Paraipaba', state='CE',
        )
        self.shelter = Shelter.objects.get(pk=10)
        self.pet_age_without_number = PetSerializer(data={
            'name': 'João Otávio',
            'age': 'esse mes',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_age_with_special_characters = PetSerializer(data={
            'name': 'João Otávio',
            'age': '21 $#@',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_age_format_incorrect = PetSerializer(data={
            'name': 'João Otávio',
            'age': '1semestre',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        
    def test_pet_age_without_number(self):
        """É Obrigatório a utilização de um número para indicar a idade de um pet"""
        self.assertFalse(self.pet_age_without_number.is_valid())
    
    def test_pet_age_with_special_characters(self):
        """O campo de idade de pet não aceita caracteres especiais"""
        self.assertFalse(self.pet_age_with_special_characters.is_valid())
    
    def test_pet_format_age(self):
        """As informações passadas no campo de idade devem seguir o sequinte formato: 00 {tempo}"""
        self.assertFalse(self.pet_age_format_incorrect.is_valid())
