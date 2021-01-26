from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()

class Apps(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=200)


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    test_field = models.IntegerField(blank=True, default=1)
