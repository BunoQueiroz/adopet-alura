from django.db import models
from tutor.models import Tutor
from django.utils import timezone
from pet.models import Pet

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.datetime.today().date().__format__('%d-%m-%Y'))

    def __str__(self) -> str:
        return f'{self.tutor} -> {self.pet}'
    