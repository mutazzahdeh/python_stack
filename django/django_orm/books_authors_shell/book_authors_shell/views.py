from django.shortcuts import render,HttpResponse,redirect
from .models import *

# Create your views here.
def index(request):
    context={
        "book":books.objects.all()
    }
    return render(request,"index.html",context)

def addbook(request):
    if request.method == "POST":
        
        books.objects.create(
        title  = request.POST['name'],
    	desc  = request.POST['desc'],
    	)
        return redirect("/")

def bookdesc(request,number):
    
    x=books.objects.get(id=number)
    y=x.author.all()
    request.session["id"]=number

    context={
        "book":books.objects.get(id=number),
        'aut':y,
        'authour':authors.objects.all()
        
    }

    return render(request,"index2.html",context)

def addaut(request):
    if request.method=='POST':
        x=books.objects.get(id=request.session["id"])
        z=authors.objects.get(id=request.POST["author"])
        y=x.author.add(z)
        return redirect(f'books/{request.session["id"]}')


    
    

