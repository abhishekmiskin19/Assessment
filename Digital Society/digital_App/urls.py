from django.urls import path
from .views import *

urlpatterns = [
    path("index1/", index1, name="index1"),
    #    Call URL====Funcation====Form Action    
    path("home/", home, name="home"),
    path("", signup_page, name="signup_page"),
    path("signin_page/", signin_page, name="signin_page"),
    path("forgot_pwd_page/", forgot_pwd_page, name="forgot_pwd_page"),
    path("otp_page/", otp_page, name="otp_page"),
    path("profile_page/", profile_page, name="profile_page"),
    path("society_members/", society_members, name="society_members"),
    path("society_watchman/", society_watchman, name="society_watchman"),
    path("notice_page/", notice_page, name="notice_page"),
    path("event_page/", event_page, name="event_page"),


    path("signup/", signup, name='signup'),
    path("signin/", signin, name='signin'),
    path("logout/", logout, name='logout'),
    path("profile_update/", profile_update, name='profile_update'),
    path("otp_creation/", otp_creation, name='otp_creation'),
    path("forgot_password/", forgot_password, name='forgot_password'),
    path("otp_send/", otp_send, name='otp_send'),
    
    path("view_notice/", view_notice, name='view_notice'),
    path("load_watchman_data/", load_watchman_data, name='load_watchman_data'),
    path("load_All_Events/", load_All_Events, name='load_All_Events'),
    path("load_All_Members/", load_All_Members, name='load_All_Members'),
    

]