#from django.db.models import Model
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length = 80)
    email =models.CharField(max_length = 220)
    dateTime = models.DateTimeField(auto_now_add = True)