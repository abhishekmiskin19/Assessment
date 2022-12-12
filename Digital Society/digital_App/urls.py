from django.urls import path
from .views import *

urlpatterns = [
    path("index1/", index1, name="index1"),
    path("home/", home, name="home"),
    path("signup_page/", signup_page, name="signup_page"),
    path("signin_page/", signin_page, name="signin_page"),
    path("forgot_pwd_page/", forgot_pwd_page, name="forgot_pwd_page"),
    
]