from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text="""<h1>Mon CV </h1> 
    <br> 
    <p>Qui suis je ? </p>"""
    return HttpResponse(text)