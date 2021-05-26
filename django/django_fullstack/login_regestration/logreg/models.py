from django.db import models
import bcrypt
import re	




# Create your models here.
class userManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['pass']) <8:
            errors["pass"] = "user pass should be at least 8 characters"
        if len(postData['name']) < 2:
            errors["name"] = "name user should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "last user should be at least 2 characters"
        return errors

class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    objects = userManager()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def creat_user(first_name,last_name, email,Password):
    return users.objects.create(first_name=first_name,last_name=last_name,email=email,Password=Password)

def get_user(email,password):
    use=users.objects.filter(email=email,Password=password)
    print(use)
    return use





