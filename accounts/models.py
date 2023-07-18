from django.db import models
from django.contrib.auth.models import AbstractUser


class CastomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
