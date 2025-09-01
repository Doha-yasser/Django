from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm

# Create your views here.
def Home(request):
    return render(request, 'user_home.html')

def Login(request):
    return render(request, 'login.html')

def Logout(request):
    return redirect('home')

def Register(request):
    # form = UserRegistrationForm()
    # return render(request, 'register.html', {'form': form})
    return HttpRequest('registed page')