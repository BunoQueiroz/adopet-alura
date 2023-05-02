from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from common.utils import add_permissions

class Shelter(User):
    name = models.CharField(max_length=50)
    borhood = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    phone = models.CharField(max_length=18, blank=True)
    image = models.ImageField(upload_to='shelters/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Shelter)
def insert_new_shelter_in_shelter_group(sender, created, instance: Shelter, **kwargs):
    if created:
        group, group_not_created = Group.objects.get_or_create(name='shelter')
        if group_not_created:
            permissions = [
                'view_tutor',
                'view_pet',
                'add_pet',
                'change_pet',
                'delete_pet',
                'view_shelter',
                'add_shelter',
                'change_shelter',
                'delete_shelter',
                'view_adoption',
                'delete_adoption',
            ]
            group_permissions = add_permissions(group, permissions)
            instance.groups.add(group_permissions)
        instance.groups.add(group)
