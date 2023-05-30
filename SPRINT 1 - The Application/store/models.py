from django.db import models
from django.contrib.auth.models import User

#create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, en_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self): 
      return self.name
    
class Product(models.Models):
   name = models.CharField(max_length=200, null=True)
   price = models.FloatField()
   digital = models.BooleanField(default=False, null=True, blank=False)
   
   def __str__(self):
      return self.name



