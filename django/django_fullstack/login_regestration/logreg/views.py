from django.shortcuts import render,HttpResponse,redirect
from . import models

# Create your views here.
def index(request):
    return render(request,"index.html")


def reg(request):

    if request.method == "POST":
        if request.POST['pass']==request.POST['cpass']:
            # users.objects.create(
            # first_name  = request.POST['name'],
            # last_name  = request.POST['lname'],
            # email = request.POST['email'],
            # Password = request.POST['pass'],)
            user=models.create_users(request.POST['name'],request.POST['lname'],request.POST['email'],request.POST['pass'])
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name

            return render(request,"welcome.html")


    return render(request,"index.html")

def logouta(request):
    return render(request,"index.html")


    
def login(request):
    if request.method == "POST":
    
        user=models.get_user(request.POST['fname'],request.POST['lname'])
        if user:
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return render(request,"welcome.html")
    return render(request,"index.html")
