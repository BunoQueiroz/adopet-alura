from django.db import models

class Shelter(models.Model):
    name = models.CharField(max_length=50)
    road = models.CharField(max_length=70, blank=True)
    number = models.PositiveIntegerField(default=1, blank=True)
    borhood = models.CharField(max_length=100, blank=True)
    CEP = models.CharField(max_length=9, blank=True)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    phone = models.PositiveBigIntegerField(default=1)
    image = models.ImageField(upload_to='shelters/%Y/%m/%d/', blank=True)

    def __str__(self):
        if self.name:
            return self.name
        return f'{self.road} - {self.city}'
