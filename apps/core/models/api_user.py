from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.utils import add_permissions


CHOICES = (
    ('f', 'FronEnd'),
    ('m', 'Mobile'),
    ('a', 'API'),
)

class APIUser(User):
    type = models.CharField(max_length=1, choices=CHOICES)
    company_or_user = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.company_or_user

@receiver(post_save, sender=APIUser,)
def insert_api_user_in_api_user_group(sender, instance: APIUser, created, **kwargs):
    group, group_not_created = Group.objects.get_or_create(name='api_user')
    if created and group_not_created:
        instance.groups.add(group)
    permissions = ['view_shelter', 'view_pet', 'view_tutor', 'add_tutor', 'add_shelter']
    group_with_permissions = add_permissions(group, permissions)
    instance.groups.add(group_with_permissions)
