from django.shortcuts import render,HttpResponse,redirect
from . import models
import bcrypt

# Create your views here.
def index(request):
    return render(request,"reg_log.html")

def registration(request):
    if request.method=="POST":
        error=models.error(request.POST)
        if len(error)>0:
            redirect ("/")
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        cpassword=request.POST["confpassword"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)   
        if cpassword==password:
            user=models.creat_user(first_name,last_name,email,pw_hash)
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect("/login")

    return redirect("/")
            
        

def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user=models.get_user(email)
      

        if user:  
            logged_user = user[0] 
            
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):

                if user:
                    request.session['id']=user[0].id
                    request.session['first_name']=user[0].first_name
                    request.session['last_name']=user[0].last_name
                    return redirect('/login')
    

    return redirect("/")

def loginre(request):
    context={
        'messages':models.get_message()
    }
    return render(request,"login.html",context)

def logout(request):
    return redirect("/")

def addmessage(request,id):
    if request.method=='POST':
        message=request.POST['message']
        messues=models.addmessage(message,id)
        return redirect("/login")
def addcomment(request,id_message,id_user):
    if request.method=='POST':
        comment=request.POST['comment']
        messues=models.addcomment(comment,id_message,id_user)
        return redirect("/login/wall")
    
def wall(request):
    context={
        'messages':models.get_message()
    }
    return render(request,"login_com.html",context)
