from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request,'NinjaGold_app/main.html') 


def process(request):
    if request.POST['building'] == 'farm':
        number = random.randrange(10, 21)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data ={
            'number' : number,
            'time' : time,
            'display' : "Earned "+str(number)+ " golds from the farm "+"("+ str(time) +")"
        }
        # request.session['gold'] += data['number']
        # request.session['activities'].append(data)
    if request.POST['building'] == 'cave':
        number = random.randrange(5, 11)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data ={
            'number' : number,
            'time' : time,
            'display' : "Earned "+str(number)+ " golds from the cave "+"("+ str(time) +")"
        }
        # request.session['gold'] += data['number']
        # request.session['activities'].append(data)
    if request.POST['building'] == 'house':
        number = random.randrange(2, 6)
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        data ={
            'number' : number,
            'time' : time,
            'display' : "Earned "+str(number)+ " golds from the house "+"("+ str(time) +")"
        }
        # request.session['gold'] += data['number']
        # request.session['activities'].append(data)
    if request.POST['building'] == 'casino':
        time = strftime("%Y-%m-%d %H:%M %p", gmtime())
        number = random.randrange(-50, 51)
        if number > 0:
            display = "Earned "+str(number)+ " golds from the casino"+"("+ str(time) +")"
        else:
            display ="Entered a casino and lost "+str(number)+ " golds"+"("+ str(time) +")"
        data ={
            'number' : number,
            'time' : time,
            'display' : display
        }
    request.session['gold'] += data['number']
    request.session['activities'].append(data)
    request.session.modified= True
    return redirect ('/')

def clear(request):
    del request.session['gold']
    del request.session['activities']
    return redirect ('/')
