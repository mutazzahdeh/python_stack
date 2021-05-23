from django.shortcuts import render,HttpResponse,redirect
from .models import dojos,ninjas

# Create your views here.
def index(request):

    context = {
        "dojos": dojos.objects.all(),
        
        }
    return render(request, "index.html", context)



def adddojo(request):
    if request.method == "POST":
        dojos.objects.create(
        name  = request.POST['name'],
    	city = request.POST['city'],
    	state = request.POST['state'],)
        return redirect("/")
    return render(request,"index.html")


def addninja(request):
    if request.method == "POST":
        x=request.POST["dojo_id"]
        y=dojos.objects.get(id=x)

        print(x)
        ninjas.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        dojo=y )
        return redirect("/")
    return render(request,"index.html")
