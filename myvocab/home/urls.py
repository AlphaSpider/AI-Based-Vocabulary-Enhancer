
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="home"),
    path('register.html',views.register,name="register"),
    path('login.html',views.loginn,name="login"),
    path('response.html',views.response,name='response')
]
