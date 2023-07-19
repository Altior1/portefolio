from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    text="""<h1>Mon CV </h1> 
    <br> 
    <p>Qui suis je ? </p>"""
    return HttpResponse(text)

def date_actuelle(request):
    return render(request,'polls/date.html', {'date':datetime.now()})