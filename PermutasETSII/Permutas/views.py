from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.

def permutas(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())