from django.shortcuts import render,HttpResponse,redirect
from .models import users


# Create your views here.
def index(request):
    context = {
    	"all_the_movies": Movie.objects.all()
    }
    return render(request,"index.html")