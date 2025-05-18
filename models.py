from django.db import models

# Create your models here.

class features(models.Model): # Here 'models' is the module that is imported from django.db. And 'Model' is the class that is imported from models.
    name= models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    text_area = models.CharField(max_length=1000)