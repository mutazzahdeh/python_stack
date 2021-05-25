from django.db import models


# Create your models here.
class showsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['network']) < 3:
            errors["desc"] = "Blog description should be at least 10 characters"
        if len(postData['description']) <10 and postData['description']!="":
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors


class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= showsManager()





