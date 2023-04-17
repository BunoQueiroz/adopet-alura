from rest_framework.test import APITestCase
from pet.serializers import PetSerializer
from shelter.models import Shelter

class PetSizeValidTestCase(APITestCase):

    def setUp(self) -> None:
        Shelter.objects.create(
            id=10, name='Abrigo Um', username='email@email.com', email='email@email.com', city='Paraipaba', state='CE',
        )
        self.shelter = Shelter.objects.get(pk=10)
        self.pet_size_valid = PetSerializer(data={
            'name': 'João Otávio',
            'age': '2 meses',
            'size': 'médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_size_with_additional_word = PetSerializer(data={
            'name': 'João Otávio',
            'age': '3 meses',
            'size': 'Mais médio',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
        self.pet_size_any_word = PetSerializer(data={
            'name': 'João Otávio',
            'age': '3 meses',
            'size': 'Qualquer',
            'characteristics': 'Energético',
            'shelter': self.shelter.pk,
        })
                
    def test_pet_size_valid(self):
        """As únicas opções em tamanho são: GRANDE, MÉDIO ou PEQUENO"""
        self.pet_size_valid.is_valid(raise_exception=False)
        self.assertRegex(self.pet_size_valid.data['size'], r'^(grande|médio|pequeno|Grande|Médio|Pequeno)$')
        
    def test_pet_with_additional_words_in_size(self):
        """Não é permitida nenhuma palavra além de: MÉDIO, PEQUENO ou GRANDE"""
        self.assertFalse(self.pet_size_with_additional_word.is_valid())

    def test_pet_word_any(self):
        """Uma palavra qualquer não deve ser válida no campo de tamanho dos pets"""
        self.assertFalse(self.pet_size_any_word.is_valid())        
