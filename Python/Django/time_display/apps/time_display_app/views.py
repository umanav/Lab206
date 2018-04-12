from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
  context = {
  "year": strftime("%m-%d-%Y", gmtime()),
  "time": strftime("%H:%M %p", gmtime())
  }
  return render(request,'time_display_app/page.html', context)