from django.shortcuts import render,HttpResponse,redirect
from .models import users


# Create your views here.
def index(request):
    context = {
    	"users": users.objects.all()
    }
    return render(request,"index.html",context)

def add(request):
 

    if request.method == "POST":
        users.objects.create(
    	first_name = request.POST['fname'],
    	Last_name = request.POST['lname'],
    	Email = request.POST['email'],
    	age = request.POST['age'],)
     
    return redirect("/")