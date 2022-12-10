from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(requst):
    return HttpResponse("<h1>Hello World</h1>")