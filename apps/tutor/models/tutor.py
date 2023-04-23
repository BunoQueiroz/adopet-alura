from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.utils import add_permissions

class Tutor(User):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


@receiver(post_save, sender=Tutor)
def insert_tutor_in_group_tutor(sender, instance: Tutor, created, **kargs):
    if created:
        group, group_not_created = Group.objects.get_or_create(name='tutor')
        if group_not_created:
            permissions = ['view_pet', 'view_shelter', 'add_tutor', 'view_tutor', 'change_tutor', 'delete_tutor']
            group_permissions = add_permissions(group, permissions)
        instance.groups.add(group_permissions)
