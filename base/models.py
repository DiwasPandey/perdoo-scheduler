from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    requestURI = models.CharField(max_length=200, null=False)
    datetime = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.name
