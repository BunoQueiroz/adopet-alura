from rest_framework import serializers
from core.models import APIUser
from core.validators import invalid_email


class APIUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIUser
        fields = ['email', 'password', 'type', 'company_or_user']

    def validate(self, data):
        if invalid_email(data['email']):
            raise serializers.ValidationError({'email': 'email inválido'})

        return data
