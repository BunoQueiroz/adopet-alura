from rest_framework import viewsets, status
from core.serializers import APIUserSerializer
from core.models import APIUser
from rest_framework.response import Response


class APIUserViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    http_method_names = ['post']
    serializer_class = APIUserSerializer
    queryset = APIUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.data
        APIUser.objects.create_user(user['email'], user['email'], user['password'], type=user['type'], company_or_user=user['company_or_user'])
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    