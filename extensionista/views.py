from django.shortcuts import render
from django.http import HttpRequest


def home(request: HttpRequest):
    return render(request, 'home.html')


def about(request: HttpRequest):
    return render(request, 'about.html')
