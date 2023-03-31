from rest_framework import viewsets, status
from tutor.models import Tutor
from tutor.serializers import TutorSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        Tutor.objects.create_user(full_name=request.POST['full_name'], username=request.POST['full_name'], email=request.POST['email'], password=request.POST['password'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        t = get_object_or_404(Tutor, email=request.data['email'])
        t.set_password(request.data['password'])
        t.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
