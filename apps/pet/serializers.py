from rest_framework import serializers
from pet.models import Pet
from pet.validators import invalid_pet_name, invalid_age_pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def validate(self, data):
        
        if invalid_pet_name(data['name']):
            raise serializers.ValidationError({'name': 'Nome de pet inválido'})
        
        if invalid_age_pet(data['age']):
            raise serializers.ValidationError({'age': 'Idade inválida'})

        return data