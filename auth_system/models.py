from django.db import models
from django.contrib.auth.models import AbstractUser

class ExtendedUser(AbstractUser):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
