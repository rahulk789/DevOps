from django.db import models

# Create your models here.

class statslist(models.Model):
    symbol = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    changeperc = models.CharField(max_length=200)
    close = models.CharField(max_length=200)
    high = models.CharField(max_length=200)
    low = models.CharField(max_length=200)
    lasttrade = models.CharField(max_length=200)

    def __str__(self):
        return self.name
