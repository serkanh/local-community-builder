from django.db import models
from swingtime.models import Event
from django.contrib.auth.models import User

class UserEvent(Event):
    user = models.ForeignKey(User, unique=True, related_name="user_profile")