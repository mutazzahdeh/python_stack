from django.shortcuts import render, HttpResponse,redirect
def index(request):
    if not('number' in request.session):
        request.session['number']=0
    request.session['number']+=1
    context={
       'number':  request.session['number']
    }

    return render(request,'index.html',context)

def destroy(request):
    request.session['number']=0
    return redirect('/')

def destroy2(request):
    return redirect('/destroy_session')

def add2(request):
    request.session['number']+=1
    return redirect('/')
def addnum(request):
    request.session['number']+=int(request.POST["number1"])-1
    return redirect('/')


