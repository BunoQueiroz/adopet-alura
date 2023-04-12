from rest_framework import serializers
from pet.models import Pet
from pet.validators import invalid_pet_name

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

    def validate(self, data):
        
        if invalid_pet_name(data['name']):
            raise serializers.ValidationError({'name': 'Nome de pet inválido'})
        
        return data