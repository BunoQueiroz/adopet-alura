from rest_framework import serializers
from pet.models import Pet
from pet.validators import invalid_name_pet, invalid_age_pet, invalid_size_pet, invalid_characteristics_pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def validate(self, data):
        
        if invalid_name_pet(data['name']):
            raise serializers.ValidationError({'name': 'Nome de pet inválido'})
        
        if invalid_age_pet(data['age']):
            raise serializers.ValidationError({'age': 'Idade inválida'})
        
        if invalid_size_pet(data['size']):
            raise serializers.ValidationError({'size': 'Tamanho não reconhecido. Tente um desses: Médio, Grande, Pequeno'})
        
        if invalid_characteristics_pet(data['characteristics']):
            raise serializers.ValidationError({'characteristics': 'Características Não aceitas'})

        return data
