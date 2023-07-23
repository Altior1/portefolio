from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    text="""
    Le texte est encore passé
    """
    return render(request,'polls/accueil.html',{'text':text})

def date_actuelle(request):
    return render(request,'polls/date.html', {'date':datetime.now()})

def projets(request):
    text="""voici la page des projets :"""
    return render(request, 'polls/projects.html', {'text':text})

def contact(request):
    text=""" """
    return render(request,'polls/contact.html',{'text':text})