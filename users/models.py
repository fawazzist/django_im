from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_purchaser = models.BooleanField(default=False)
    is_warehouse = models.BooleanField(default=False)
    is_production = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username



