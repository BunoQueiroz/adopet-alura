from rest_framework import serializers
from tutor.models import Tutor
from .validators import different_passwords, weak_password, full_name_invalid

class TutorSerializer(serializers.ModelSerializer):
    
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = Tutor
        fields = ['full_name', 'email', 'password', 'confirm_password']
    
    def validate(self, data):
        if weak_password(data['password']):
            raise serializers.ValidationError('A senha é muito fraca')
        if different_passwords(data['password'], data['confirm_password']):
            raise serializers.ValidationError('As senhas passadas NÃO podem ser diferentes')
        if full_name_invalid(data['full_name']):
            raise serializers.ValidationError('O nome passado não é válido')
        return data
