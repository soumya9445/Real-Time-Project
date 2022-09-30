from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.showindex,name='main'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
    path('validate_otp/',views.validate_otp,name='validate_otp'),

    #otp-page
    path('user_otp/',views.userotp,name='user_otp'),
    #conformation
    path('conformation/',views.conformation,name='conformation'),
    #login page
    path('login/',views.login,name='login'),
    path('login_check/',views.logincheck,name='login_check'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('logout/',views.logout,name='logout'),
]

