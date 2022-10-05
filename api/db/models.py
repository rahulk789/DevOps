from django.db import models

# Create your models here.

class stats(models.Model):
    Symbol = models.CharField(max_length=200)
    Last = models.IntegerField(default=0)
    Change = models.IntegerField(default=0)
    Changeperc = models.IntegerField(default=0)
    Close = models.IntegerField(default=0)
    High = models.IntegerField(default=0)
    Low = models.IntegerField(default=0)
    LastTrade = models.DateTimeField('date published')

