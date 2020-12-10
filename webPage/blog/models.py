#from django.db.models import Model
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length = 80)
    email =models.CharField(max_length = 220)
    dateTime = models.DateTimeField(auto_now_add = True)


class Noticias(models.Model):
    title = models.CharField(max_length = 80)
    subtitle = models.CharField(max_length = 220)
    description = models.TextField()
    location = models.CharField(max_length = 100)
    date = models.CharField(max_length = 30)
    dataTime = models.DateTimeField(auto_now_add = True)