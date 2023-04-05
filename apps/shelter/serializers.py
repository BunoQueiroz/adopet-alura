from rest_framework import serializers
from shelter.models import Shelter
from shelter.validators import invalid_name_shelter, invalid_name_city, invalid_format_cep, invalid_name_road

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

    def validate(self, data):
        if invalid_name_shelter(data['name']):
            raise serializers.ValidationError({'name': 'O nome deve conter ao menos uma letra'})
        
        if invalid_name_city(data['city']):
            raise serializers.ValidationError({'city': 'Nome de cidade inválido'})

        if invalid_format_cep(data['CEP']):
            raise serializers.ValidationError({'CEP': 'CEP de formato inválido. Siga o formato: xxxxx-xxx'})

        if invalid_name_road(data['road']):
            raise serializers.ValidationError({'road': 'Rua não prevista em nossas análises'})

        return data
