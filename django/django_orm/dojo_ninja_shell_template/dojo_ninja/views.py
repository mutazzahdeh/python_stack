from django.shortcuts import render,HttpResponse,return

# Create your views here.
def index(request):
    return render(request,"index")
