from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name = 'uprofile')
    avatar = models.URLField(default="http://placehold.it/64x64",verbose_name = u"Image")

# Create your models here.
