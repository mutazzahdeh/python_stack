from django.db import models


# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class car(models.Model):
    name = models.CharField(max_length=255)
    model = models.IntegerField()
    clints = models.ManyToManyField(users,related_name="cars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_users(first_name,last_name, email,Password):
    return users.objects.create(first_name=first_name,last_name=last_name,email=email,Password=Password)

def get_user(email,password):
    use=users.objects.filter(email=email,Password=password)
    print(use)
    return use[0]

