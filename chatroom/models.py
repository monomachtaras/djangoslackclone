from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone


class CustomUser(AbstractUser):
    """" this is our base user class    """

    activation_key = models.CharField(max_length=64, blank=True)
    image = models.ImageField(blank=True)
    email = models.EmailField(blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.email}"
