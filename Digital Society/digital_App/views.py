from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse


# Create your views here.

default_data = {

}


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

# Profile Page Update Logic
def profile_update(request):
    print(request.POST)
    user = User.objects.get(Email = request.session['email'])
    member = Member.objects.get(User = user)

    member.FullName = ' '.join(request.POST['first_name'],request.POST['last_name'],)
    member.Mobile = request.POST['mobile']
    member.Birthday = request.POST['birthdate']
    member.Gender = request.POST['gender']

    member.save()

    return redirect(profile_page)


# Load Profile data Logic
def profile_data(request):
    print(request.POST)
    user = User.objects.get(Email = request.session['email'])
    member = Member.objects.get(User = user)

    member.first_name = member.FullName.split()[0]
    member.last_name = member.FullName.split()[1]

    member.birthday = member.Birthday.strftime("%Y-%m-%d") 

    default_data["member_data"]= member




