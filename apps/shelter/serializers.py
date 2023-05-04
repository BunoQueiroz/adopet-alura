from rest_framework import serializers
from shelter.models import Shelter
from shelter.validators import invalid_name_shelter, invalid_state
from shelter.validators import invalid_borhood, invalid_phone, invalid_name_city
from shelter.validators import invalid_email
from common.utils import field_requireds
from common.validators import invalid_password


class ShelterSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Shelter
        fields = ['id', 'name', 'email', 'password', 'confirm_password', 'phone', 'city', 'state', 'borhood']

    def validate(self, data):

        expected_fields = ['name', 'email', 'password', 'confirm_password', 'phone', 'city', 'state', 'borhood']
        field_requireds(expected_fields, data)

        if invalid_name_shelter(data['name']):
            raise serializers.ValidationError({'name': 'O nome deve conter ao menos uma letra'})
        
        if invalid_name_city(data['city']):
            raise serializers.ValidationError({'city': 'Nome de cidade inválido'})
        
        if invalid_state(data['state']):
            raise serializers.ValidationError({'state': 'Este estado não é válido. Segue o exemplo: CE'})

        if invalid_borhood(data['borhood']):
            raise serializers.ValidationError({'borhood': 'Nome de bairro inválido'})

        if invalid_phone(data['phone']):
            raise serializers.ValidationError({'phone': 'Número inválido. Segue o exemplo: (85)91234-1234'})

        if invalid_email(data['email']):
            raise serializers.ValidationError({'email': 'Email inválido'})
        
        if invalid_password(data['password']):
            raise serializers.ValidationError({'password': 'Por favor, escreva senhas mais fortes com, pelo menos, 8 caracteres'})

        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'As senhas devem ser exatamente iguais'})

        return data
