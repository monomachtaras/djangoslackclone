from django.db import models
from django.contrib.auth.models import User


class ChatUser(models.Model):
    """" this is our base user class    """

    user = models.OneToOneField(User)

    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"




