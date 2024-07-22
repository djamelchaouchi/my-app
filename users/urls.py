from django.urls import path
from .import views
from django.contrib import admin
from .views import *

urlpatterns = [
path('login/', views.signin, name='login' ),
path('register/', views.register, name='register' ),
path('logout/', views.logoutt, name='logout' ),

]