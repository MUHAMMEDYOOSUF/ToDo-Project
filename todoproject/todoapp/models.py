from django.db import models


# Create your models here.

class task(models.Model):
    task = models.CharField(max_length=250)
    priority = models.IntegerField()
    date=models.DateField()


