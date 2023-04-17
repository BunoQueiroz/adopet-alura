from rest_framework import serializers
from shelter.models import Shelter
from shelter.validators import invalid_name_shelter, invalid_state
from shelter.validators import invalid_borhood, invalid_phone, invalid_name_city

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = ['name', 'password', 'email', 'phone', 'city', 'state', 'borhood']

    def validate(self, data):
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

        return data
