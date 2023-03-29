from rest_framework import viewsets, status
from tutor.models import Tutor
from tutor.serializers import TutorSerializer
from rest_framework.response import Response

class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        Tutor.objects.create_user(full_name=request.POST['full_name'], username=request.POST['full_name'], email=request.POST['email'], password=request.POST['password'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
