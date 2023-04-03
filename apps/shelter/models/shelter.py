from django.db import models

class Shelter(models.Model):
    name = models.CharField(max_length=50, blank=True)
    road = models.CharField(max_length=70)
    number = models.PositiveIntegerField(default=1)
    borhood = models.CharField(max_length=100)
    CEP = models.CharField(max_length=9)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)

    def __str__(self):
        if self.name:
            return self.name
        return f'{self.road} - {self.city}'
