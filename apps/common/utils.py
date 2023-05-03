from django.contrib.auth.models import Permission, Group
from rest_framework import serializers


def add_permissions(group: Group, permissions: list) -> Group:
    for perm in permissions:
        permission = Permission.objects.get(codename=perm)
        group.permissions.add(permission)
    return group

def field_requireds(expected_fields: list, data) -> None:
    for field in expected_fields:
        if not field in data.keys():
            raise serializers.ValidationError({f'{field}': f'O campo {field} não pode ser nulo ou vazio'})
