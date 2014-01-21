from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    event = models.ForeignKey(Event)

