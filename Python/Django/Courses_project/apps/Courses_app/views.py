# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    return render(request,'Courses_app/main.html', {'courses' : Course.objects.all()})

def destroy_confirm(request,id):
    return render(request,'Courses_app/remove.html', {'courses' : Course.objects.get(id=id)})

def destroy(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')

def add(request):
    errors = Course.objects.basic_validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.create(name =name, description = description) 
        return redirect('/')