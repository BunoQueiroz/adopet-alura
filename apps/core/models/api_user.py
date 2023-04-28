from django.contrib.auth.models import User
from django.db import models


CHOICES = (
    ('f', 'FronEnd'),
    ('m', 'Mobile'),
    ('a', 'API'),
)

class APIUser(User):
    type = models.CharField(max_length=1, choices=CHOICES)
    company_or_user = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.company_or_user
