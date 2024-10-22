from django.db import models

class tienda(models.Model):
    nombre=models.CharField(max_length=50)
    razonsocial=models.CharField(max_length=70)
    rutempresa=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    numerocasa=models.IntegerField()
# Create your models here.
