from rest_framework import viewsets
from core.serializers import APIUserSerializer
from core.models import APIUser


class APIUserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    http_method_names = ['post']
    serializer_class = APIUserSerializer
    queryset = APIUser.objects.all()
