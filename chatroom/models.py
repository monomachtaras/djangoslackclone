from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone


class CustomUser(AbstractUser):
    """" this is our base user class    """

    password = models.CharField(min_length=8, max_length=128)
    activation_key = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True)

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.email}"


class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now(), db_index=True)
