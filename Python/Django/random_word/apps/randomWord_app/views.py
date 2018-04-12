# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    unique_id = get_random_string(length=14)
    word = {
        "word" : unique_id,
    }
    return render(request,'randomWord_app/random_word.html', word)

def reset(request):
    del request.session['counter']
    return redirect('/')