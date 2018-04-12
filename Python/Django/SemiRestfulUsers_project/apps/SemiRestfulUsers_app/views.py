# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    return redirect('/users')

def users(request):
    return render(request,'SemiRestfulUsers_app/main.html', {'users' : User.objects.all()})

def add(request):
    response = "placeholder to later display all the list of blogs"
    return render(request, 'SemiRestfulUsers_app/new.html')

def view_user(request, id):
    return render(request,'SemiRestfulUsers_app/user.html', {'user' : User.objects.get(id=id)})

def edit_user(request, id):
    return render(request,'SemiRestfulUsers_app/edit.html', {'user' : User.objects.get(id=id)})

def update(request):
    id = request.POST['id']
    errors = User.objects.basic_validator(request.POST)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/'+id+'/edit')
    else:
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        user = User.objects.get(id=id)
        user.full_name = name
        user.email = email
        user.save()
        return redirect('/users/'+id+'')

def create(request):
    name = request.POST['name']
    email = request.POST['email']
    User.objects.create(full_name =name, email = email) 
    id = User.objects.last().id
    id = str(id)
    print id
    return redirect('/users/'+id+'')

def destroy(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/users/')
