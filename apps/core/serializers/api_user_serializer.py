from rest_framework import serializers
from core.models import APIUser


class APIUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = APIUser
        fields = ['email', 'password', 'type', 'company_or_user']
