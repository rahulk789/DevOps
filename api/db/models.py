from django.db import models

# Create your models here.

class statslist(models.Model):
    Symbol = models.CharField(max_length=200)
    Last = models.CharField(max_length=200)
    Change = models.CharField(max_length=200)
    Changeperc = models.CharField(max_length=200)
    Close = models.CharField(max_length=200)
    High = models.CharField(max_length=200)
    Low = models.CharField(max_length=200)
    LastTrade = models.CharField(max_length=200)

