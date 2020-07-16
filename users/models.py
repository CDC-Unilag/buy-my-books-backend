from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={
            'unique': _('A user with that email already exists.'),
        }, db_index=True)

    REQUIRED_FIELDS = ['email']


class Account(models.Model):
    types = (
            ('B', 'BUYER'), ('S', 'SELLER')
            )
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    user_type = models.CharField(max_length=12, choices=types)


