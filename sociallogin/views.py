from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

#로그인 페이지
def login(request):
    return render(request, 'sociallogin/login.html')

def signup(request):
    return render(request, 'sociallogin/signup.html')

def find_pass(request):
    return render(request, 'sociallogin/find_pass.html')

# Create your views here.
