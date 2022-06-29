from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse

from app.views import homepage, success

urlpatterns = [
    path('', homepage, name='home'),
    path('success/', success, name='success')
]
