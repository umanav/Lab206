# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    return render(request,'SurveyForm/index.html')

def process(request):
    request.session['counter'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    
    return redirect ('/result')

def result(request):
    return render(request,'SurveyForm/result.html')

