from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse('<h1>hello user</h1>')

def Login(request):
    # return HttpResponse('<h1>login page<h1>')
    return render(request, 'html/login.html')

def Logout(request):
    return HttpResponse('<h1>logout page<h1>')


def Register(request):
    return HttpResponse('<h1>Register page<h1>')