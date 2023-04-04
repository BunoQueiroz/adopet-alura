from rest_framework import serializers
from shelter.models import Shelter
from shelter.validators import invalid_name_shelter

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

    def validate(self, data):
        if invalid_name_shelter(data['name']):
            raise serializers.ValidationError({'name': 'O nome deve conter ao menos uma letra e não pode possuir espaços antes ou depois dos caracteres que o seu nome necessitam'})
        return data
    