from rest_framework import serializers
from tutor.models import Tutor
from .validators import full_name_invalid, email_invalid
from common.utils import field_requireds
from common.validators import invalid_password


class TutorSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Tutor
        fields = ['id', 'full_name', 'email', 'password', 'confirm_password']
    
    def validate(self, data):
        
        expected_fields = ['full_name', 'email', 'password', 'confirm_password']
        field_requireds(expected_fields, data)

        if invalid_password(data['password']):
            raise serializers.ValidationError({'password': 'A senha é muito fraca'})
        
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'As senhas passadas NÃO podem ser diferentes'})
        
        if full_name_invalid(data['full_name']):
            raise serializers.ValidationError({'full_name': 'O nome passado não é válido'})
        
        if email_invalid(data['email']):
            raise serializers.ValidationError({'email': 'Endereço de email inválido'})

        return data
