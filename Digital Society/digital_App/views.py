from django.shortcuts import render,redirect
from django.http import HttpResponse


# Create your views here.

def index1(request):
    return HttpResponse("<h1>Hello World</h1>")
    
def home(request):
    return render(request, "home.html")

def signup_page(request):
    return render(request, "signup_page.html")

def signin_page(request):
    return render(request, "signin_page.html")

def forgot_pwd_page(request):
    return render(request, "forgot_pwd_page.html")

