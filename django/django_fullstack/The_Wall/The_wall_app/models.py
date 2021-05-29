from django.db import models
import re

# Create your models here.
class usersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(postData['first_name']) < 5:
            errors["first_name"] = "First name Should be at least 5 characters"
        if len(postData['last_name']) < 5:
            errors["last_name"] = "laste name should be at least 10 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"

        return errors

class users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    objects=usersManager()

class messsages(models.Model):
    messages = models.TextField()
    user_id=models.ForeignKey(users, related_name="messsage", on_delete = models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class comments(models.Model):
    comment = models.TextField()
    message_id=models.ForeignKey(messsages, related_name="comments", on_delete = models.CASCADE)
    user_id=models.ForeignKey(users, related_name="comments", on_delete = models.CASCADE)
    creat_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    




def creat_user(first_name,last_name,email,password):
    user=users.objects.create(first_name=first_name,last_name=last_name,email=email,password=password)
    return user

def get_user(email):
    user=users.objects.filter(email=email)
    return user

def error(postData):
    errors=users.objects.basic_validator(postData)
    return errors

def addmessage(message,id):
    user=users.objects.get(id=id)
    mess= messsages.objects.create(messages=message,user_id=user)
    return mess
def get_message():
    return messsages.objects.all().order_by("-creat_at")


def addcomment(comment,id_mas,id_user):
    user=users.objects.get(id=id_user)
    mess=messsages.objects.get(id=id_mas)
    comment= comments.objects.create(comment=comment,user_id=user,message_id=mess)
    return comment
