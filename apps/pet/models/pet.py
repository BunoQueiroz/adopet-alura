from django.db import models
from shelter.models import Shelter

class Pet(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pet/%Y/%m/%d/', blank=True)
    age = models.CharField(max_length=10)
    size = models.CharField(max_length=15)
    characteristics = models.CharField(max_length=25)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
