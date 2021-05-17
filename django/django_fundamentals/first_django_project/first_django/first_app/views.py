from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

def index(request):
    mydict = {
        'first': 123,
        'second': 456
    }
    context = {
        'mydict': mydict
    }
    return render(request, 'index.html', context)


def check_credantial(username, passwd):
    if username == "khalil" and passwd == "123456":
        return True
    return False


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passwd']
        if check_credantial(username, passwd):
            context = {
                'name': 'Khalil Khalil'
            }
            return redirect('/home')
    return redirect('/')


def home(request):
    context = {
                'name': 'Khalil Khalil'
            }
    return render(request, 'home.html', context)


