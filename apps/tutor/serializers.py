from rest_framework import serializers
from tutor.models import Tutor

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['full_name', 'email', 'password']
