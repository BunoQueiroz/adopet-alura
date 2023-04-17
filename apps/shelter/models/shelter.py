from django.db import models
from django.contrib.auth.models import User

class Shelter(User):
    name = models.CharField(max_length=50)
    borhood = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    phone = models.CharField(max_length=18, blank=True)
    image = models.ImageField(upload_to='shelters/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name
