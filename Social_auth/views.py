from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def login(request):
    print(request)
    if request.METHOD=='POST':
        print(request)
