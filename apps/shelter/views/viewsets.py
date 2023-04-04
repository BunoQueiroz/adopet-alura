from rest_framework import viewsets
from shelter.serializers import ShelterSerializer
from shelter.models import Shelter

class ShelterViewSet(viewsets.ModelViewSet):
    serializer_class = ShelterSerializer
    queryset = Shelter.objects.all()
