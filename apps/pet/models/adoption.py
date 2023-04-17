from django.db import models
from tutor.models import Tutor
from django.utils import timezone
from pet.models import Pet

class Adoption(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.datetime.today().date().__format__('%d-%m-%Y'))

    def __str__(self) -> str:
        return f'{self.tutor} -> {self.pet}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.pet.adopted = True
        self.pet.save()
        return super().save(force_insert, force_update, using, update_fields)
    
    def delete(self, using=None, keep_parents=False) -> None:
        self.pet.adopted = False
        self.pet.save()
        super(Adoption, self).delete(using, keep_parents)
    