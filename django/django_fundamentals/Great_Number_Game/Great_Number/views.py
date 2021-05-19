from django.shortcuts import render,HttpResponse,redirect
import random 	
# Create your views here.
def index(request):
    
    if not("rand" in request.session) :
        request.session["rand"]=random.randint(1, 100)
        print(request.session["rand"])
    return render(request,"index.html")

def num(request):
    request.session["num"]=int(request.POST["number1"])
    request.session["bool"]=True
    return redirect("/")



def plyagine(request):
    request.session["rand"]=random.randint(1, 100)
    print(request.session["rand"])
    request.session["bool"]=False
    return redirect("/")
