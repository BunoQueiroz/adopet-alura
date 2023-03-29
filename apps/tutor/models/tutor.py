from django.db import models
from django.contrib.auth.models import User

class Tutor(User):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
