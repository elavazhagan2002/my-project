from django.db import models

# Create your models here.

class employee(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    salary = models.DecimalField(max_digitss=10,decimal_places=2, default=0)


