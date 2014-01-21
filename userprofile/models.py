from django.db import models
from django.contrib.auth.models import User
from swingtime.models import Event


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    event = models.ForeignKey(Event)


