from rest_framework import viewsets, status
from shelter.serializers import ShelterSerializer
from shelter.models import Shelter
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ShelterViewSet(viewsets.ModelViewSet):
    serializer_class = ShelterSerializer
    queryset = Shelter.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        Shelter.objects.create_user(username=data['email'], email=data['email'], password=data['password'], city=data['city'], state=data['state'], name=data['name'], borhood=data['borhood'], phone=data['phone'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    