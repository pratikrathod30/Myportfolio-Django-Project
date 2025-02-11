from django.contrib import admin,messages
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name='home'),
    path('contactform/', views.index, name='contactform'),
]

