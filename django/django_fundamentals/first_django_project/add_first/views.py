from django.shortcuts import render, HttpResponse,redirect
import json
def root(request):
    return redirect ("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect ("/")
def show(request,number):
    return HttpResponse("placeholder to display blog number "+str(number))
def edit(request,number):
    return HttpResponse("placeholder to display blog number {"+number+"}")
def destroy(request,number):
    return redirect ("/blogs")
def destroy(request):
    return redirect ("/blogs")
def act(request):
    d={
        "titel":"My first Blog",
        "content":"sdafsfsdfsdf"}
    return JsonResponse(d)

# Create your views here.
