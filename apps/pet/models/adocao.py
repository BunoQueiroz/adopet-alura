from django.db import models
from tutor.models import Tutor
from datetime import date
from pet.models import Pet

class Adocao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

    def __str__(self) -> str:
        return f'{self.tutor} -> {self.pet}'
    