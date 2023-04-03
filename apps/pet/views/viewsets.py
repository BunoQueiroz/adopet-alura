from rest_framework import viewsets
from pet.serializers import PetSerializer
from pet.models import Pet

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
