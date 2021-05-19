from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if not('number' in request.session):
        request.session['number']=0
    request.session['number']+=1
 

    return render(request,'index.html')

def destroy(request):
    request.session['number']=0
    return redirect('/')

def add2(request):
    request.session['number']+=1
    return redirect('/')
def addnum(request):
    
    request.session['number']+=int(request.POST["number1"])-1
    return redirect('/')


