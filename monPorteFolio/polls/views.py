from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    text="""
    le Texte est passé
    """
    return render(request,'polls/accueil.html',{'text':text})

def date_actuelle(request):
    return render(request,'polls/date.html', {'date':datetime.now()})