from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model  # ex) models.ForeignKey(get_user_model(), ...)
from django.conf import settings


# using a custom user model
class User(AbstractUser):
    pass
