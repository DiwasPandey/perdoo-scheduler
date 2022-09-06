from django.db import models
from django.contrib.auth.models import User
# from django.db.models import JSONField
from django.forms.models import model_to_dict

# Method options 
GET = "GET"
POST = "POST"
PUT = "PUT"
DELETE = "DELETE"

METHOD_CHOICES = [
    (POST, 'POST'),
    (GET, 'GET'),
    (PUT, 'PUT'),
    (DELETE, 'DELETE'),
]
# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    requestMethod = models.CharField(max_length = 6, choices=METHOD_CHOICES, default=POST)
    requestURI = models.URLField(max_length=500)
    params = models.JSONField(verbose_name='params', default=dict, blank=True, null=True)
    datetime = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return self.name

    def toJSON(self) -> dict:
        eventJSON = {}
        eventJSON['user'] = model_to_dict(self.user)
        eventJSON['name'] = self.name
        eventJSON['method'] = self.requestMethod
        eventJSON['requestURI'] = self.requestURI
        eventJSON['datetime'] = self.datetime

        return eventJSON