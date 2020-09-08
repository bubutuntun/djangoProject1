from django.db import models


# Create your models here.
class Stduent(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=20)
