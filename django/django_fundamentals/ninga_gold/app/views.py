
from __future__ import unicode_literals
import datetime
import random
from django.shortcuts import render, redirect

# Create your views here.
def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return render(request,'index.html')

def home(request, id):
    """
    Describe
    id: the book id
    par2:
    return:: render the index.html page
    """
    try:
        request.session['gold'] # why?
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            
            earnings = random.randrange(10, 20)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the farm! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "cave":
           
            earnings = random.randrange(5, 10)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the cave! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "house":
            
            earnings = random.randrange(2, 5)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
           
            return redirect('/')
        elif request.POST['action'] == "casino":
            
            earnings = random.randrange(-50, 50)
            request.session['gold'] += earnings
            if earnings < 0:
                request.session['activities'].append(
                    'Entered a casino and Won ' + str(earnings) + ' gold! Ouch! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 8:
                    request.session['activities'].pop(0)
                return redirect('/')
            else:
                request.session['activities'].append(
                    'Entered a casino and Lost ' + str(earnings) + ' gold. Holy Cow! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 8:
                    request.session['activities'].pop(0)
                return redirect('/')
    else:
        return redirect('/')
