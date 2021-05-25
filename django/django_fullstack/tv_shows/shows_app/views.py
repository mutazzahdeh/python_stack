from django.shortcuts import render,redirect
from .models import *
from time import gmtime, strftime
# Create your views here.
def index(request):
    context = {
        "all_the_shows" : shows.objects.all()
    }
    return render(request,"shows.html",context)

def view_show(request, show_id):
    this_show = shows.objects.get(id = int(show_id))
    context = {
        "all_the_shows" : shows.objects.all(),
        "this_show" : this_show
    }
    return render(request,"view_show.html", context)


def add_show(request):
    if request.method=="POST":
        add_show = shows.objects.create(title=request.POST["title"],network=request.POST["network"],release_date=request.POST["date"],description =request.POST['description'])
        return redirect(f"show/{add_show.id}")

def new(request):
    return render(request,"add_show.html",)

def edit_show(request, show_id):
    this_show = shows.objects.get(id = int(show_id))
    date = this_show.release_date
    newDate = date.strftime("%Y-%m-%d")
    context = {
        "this_show" : this_show,
        "newDate" : newDate,
        }
    return render(request,"edit_show.html",context)

def edit(request,show_id):
    this_show = shows.objects.get(id = int(show_id))
    if request.method=="POST":
        this_show.title=request.POST["title"]
        this_show.network=request.POST["network"]
        this_show.release_date=request.POST["date"]
        this_show.description =request.POST['description']
        this_show.save()
        return redirect(f"/show/{show_id}")

def delete(request,show_id):
    this_show = shows.objects.get(id = int(show_id))
    this_show.delete()
    return redirect('/shows')


