from django.shortcuts import render,redirect
from .models import *
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

def profile_page(request):
    return render(request, 'profile_page.html')

# Signup Logic
def signup(request):
    print(request.POST)
    password = request.POST['password']

    if password == request.POST['conform_password']:
        user = User.objects.create(Email = request.POST['email'], Password = password)
        Member.objects.create(User = user)
        print("Signup successfully...")

    else:
        print('both password should be same...')
        return redirect(signup_page)

    return redirect(signin_page)

# Signin Logic

def signin(request):
    # print(request.POST)
    try:
        user = User.objects.get(Email = request.POST['email'])
        if user.Password == request.POST['password']:
            request.session['email'] = user.Email
            return redirect(home)
        else:
            return render(request, 'signin_page', {'error': "Password does not match"})

    except User.DoesNotExist as err:
        return render(request, 'signin_page', {'error': "Password does not match"})


# Logout Logic
def logout(request):
    print(request.POST)
    if 'email' in request.session:
        del request.session['email']
        return redirect(signin_page)
    return redirect(home)


