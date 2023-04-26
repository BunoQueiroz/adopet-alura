from rest_framework import viewsets
from pet.serializers import PetSerializer, AdoptionSerializer
from pet.models import Pet, Adoption
from rest_framework.permissions import IsAuthenticated

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.filter(adopted=False)

class AdoptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AdoptionSerializer
    queryset = Adoption.objects.all()
