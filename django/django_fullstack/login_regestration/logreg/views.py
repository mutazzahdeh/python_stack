from django.shortcuts import render,HttpResponse,redirect
from . import models

from .models import *
import bcrypt


# Create your views here.
def index(request):
    request.session["bool"]=False
    return render(request,"index.html")


def reg(request):

    if request.method == "POST":
        errors = users.objects.basic_validator(request.POST)
        if len(errors)==0:

            if request.POST['pass']==request.POST['cpass']:

                password = request.POST['pass']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()    
                print(pw_hash) 
                user =users.objects.create(
                first_name  = request.POST['name'],
                last_name  = request.POST['lname'],
                email = request.POST['email'],
                Password = pw_hash)   
                
                request.session['id']=user.id
                request.session['first_name']=user.first_name
                request.session['last_name']=user.last_name

                return redirect('/addn')
        else:
            request.session["bool"]=True
            context={
                'errors':errors 
                
            }
            return render(request,"index.html",context)



    return render(request,"index.html")

def logouta(request):
    return render(request,"index.html")


def welcome(request):
    return render(request,"welcome.html")


    
def login(request):
    if request.method == "POST":
        user = models.get_user(request.POST['fname'],request.POST['lname']) 
        if user:  
            logged_user = user[0] 
            
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):

                if user:

                    request.session['id']=user[0].id
                    request.session['first_name']=user[0].first_name
                    request.session['last_name']=user[0].last_name
                    return render(request,"welcome.html")
                    
                   
        
        
        
    return redirect("/login")

def logina(requst):
    return redirect("/login")
