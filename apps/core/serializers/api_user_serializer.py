from rest_framework import serializers
from core.models import APIUser
from core.validators import invalid_company_or_user
from common.validators import invalid_password, invalid_email
from common.utils import field_requireds


class APIUserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = APIUser
        fields = ['email', 'password', 'confirm_password', 'type', 'company_or_user']

    def validate(self, data):
        
        expected_fields = ['email', 'password', 'confirm_password', 'type', 'company_or_user']
        field_requireds(expected_fields, data)

        if invalid_email(data['email']):
            raise serializers.ValidationError({'email': 'email inválido'})
        
        if invalid_password(data['password']):
            raise serializers.ValidationError({'password': 'Senha muito fraca'})
        
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'As senhas não podem ser diferentes'})
        
        if invalid_company_or_user(data['company_or_user']):
            raise serializers.ValidationError({'company_or_user': 'Usuário ou compania inválida'})

        return data
