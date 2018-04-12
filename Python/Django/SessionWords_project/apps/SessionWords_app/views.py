from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime


def index(request): 
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request,'SessionWords_app/session_words.html')
    

def add(request):
    data={
        'word' : request.POST['new_word'],
        'color' : request.POST['color'],
        'date' : strftime("%m-%d-%Y %H:%M %p", gmtime()),
        'font': request.POST.get('font')
    }
    request.session['words'].append(data)
    request.session.modified= True
    print request.session['words']
    return redirect ('/')

def clear(request):
    del request.session['words']
    return redirect ('/')
