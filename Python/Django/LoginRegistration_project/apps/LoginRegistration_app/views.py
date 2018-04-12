# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
# Create your views here.
def index(request):
    if 'id' in request.session == None:
        return redirect('/succcess')
    if 'id' in request.session:
        return redirect('/succcess')
    return render(request,'LoginRegistration_app/main.html')
    

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['id'] = User.objects.last().id
        return redirect('/succcess')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['id'] = user.id
        return redirect('/succcess')

def logout(request):
    del request.session['id']
    return redirect('/')

def profile(request):
    id=request.session['id']
    return render(request,'LoginRegistration_app/profile.html', {'user' : User.objects.get(id=id)})