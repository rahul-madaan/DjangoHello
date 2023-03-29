from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from hellodjango import views

# Create your views here.

def index(request):
    context = {
        'variable': 'this is variable'
    }
    return render(request, 'index.html', context)
#
# def index(request):
#     return HttpResponse("This is homepage")


def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse("This is services page")