from rest_framework import viewsets
from pet.serializers import PetSerializer, AdoptionSerializer
from pet.models import Pet, Adoption

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()

class AdoptionViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'get']
    serializer_class = AdoptionSerializer
    queryset = Adoption.objects.all()
