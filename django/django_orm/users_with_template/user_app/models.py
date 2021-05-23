
from django.db import models
    
class users(models.Model):
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Email =models.CharField(max_length=255)
    age = models.IntegerField()
 