from django.urls import path
from .views import *

urlpatterns = [
    path("index1/", index1, name="index1"),
    #    Call URL====Funcation====Form Action    
    path("home/", home, name="home"),
    path("", signup_page, name="signup_page"),
    path("signin_page/", signin_page, name="signin_page"),
    path("forgot_pwd_page/", forgot_pwd_page, name="forgot_pwd_page"),
    path("profile_page/", profile_page, name="profile_page"),

    path("signup/", signup, name='signup'),
    path("signin/", signin, name='signin'),
    path("logout/", logout, name='logout'),
    path("profile_update/", profile_update, name='profile_update'),


]