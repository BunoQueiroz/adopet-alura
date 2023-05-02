from django.contrib.auth.models import Permission, Group

def add_permissions(group: Group, permissions: list) -> Group:
    for perm in permissions:
        permission = Permission.objects.get(codename=perm)
        group.permissions.add(permission)
    return group
