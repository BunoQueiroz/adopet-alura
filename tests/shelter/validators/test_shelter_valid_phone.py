from rest_framework.test import APITestCase
from shelter.serializers import ShelterSerializer


class ShelterPhoneValidTestCase(APITestCase):

    def setUp(self) -> None:
        self.shelter_number_with_letter = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': 'meu telefone01',
            'CEP': '62685-000',
            'number': '',
            'road': 'rua joão',
            'borhood': 'bairro fulano',
        })
        self.shelter_number_negative = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '-852200000',
            'CEP': '62685-000',
            'number': '',
            'road': 'rua joão',
            'borhood': 'bairro fulano',
        })
        self.shelter_number_tiny = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'city': 'Paraipaba',
            'state': 'CE',
            'road': 'rua joão',
            'phone': '11900000000',
            'CEP': '62685-000',
            'number': '',
            'borhood': 'bairro fulano'
        })
        self.shelter_number_very_large = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'CEP': '62685-000',
            'number': '',
            'road': 'rua joão',
            'borhood': 'bairro fulano',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '5699999999999',
        })
        self.shelter_number_valid_with_ddd = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'CEP': '62685-000',
            'number': '',
            'road': 'rua joão',
            'borhood': 'bairro fulano',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '(85)98163-9630',
        })
        self.shelter_number_valid_with_ddd_and_nc = ShelterSerializer(data={
            'name': 'Abrigo de exemplo',
            'CEP': '62685-000',
            'number': '',
            'road': 'rua joão',
            'borhood': 'bairro fulano',
            'city': 'Paraipaba',
            'state': 'CE',
            'phone': '+55 (85)98163-9630',
        })

    def test_shelter_phone_with_letters(self):
        """Não é permitida a utilização de letras no campo de número de telefone"""
        self.assertFalse(self.shelter_number_with_letter.is_valid())

    def test_shelter_phone_negative(self):
        """Não são permitidos números negativos no campo de telefone dos abrigos"""
        self.assertFalse(self.shelter_number_negative.is_valid())

    def test_shelter_phone_with_number_valid(self):
        """Os números não devem ser menores que 11910000000. Nem maiores que 5599999999999"""
        self.assertFalse(self.shelter_number_tiny.is_valid())
        self.assertFalse(self.shelter_number_very_large.is_valid())

    def test_shelter_phone_valids(self):
        """Os telefones com ddd e/ou código nascional devem ser considerados válido"""
        self.assertTrue(self.shelter_number_valid_with_ddd.is_valid())
        self.assertTrue(self.shelter_number_valid_with_ddd_and_nc.is_valid())
