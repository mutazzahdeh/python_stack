from django.shortcuts import render, HttpResponse,redirect


def index(request):
    return render(request,"index.html")


def result(request):
    
    context={ 'name': request.POST['name'],
    
    'location': request.POST['location'],
    
    "lang" : request.POST['lang'],
    
    "comment": request.POST['text']
    }

    return render(request,"index2.html",context)

def goback(request):
    return redirect('/')

   
    