
from django.db import models

# Create your models here.

class Quotes(models.Model):
    Quoation = models.CharField(max_length=1000)
    Author = models.CharField(max_length=100)
