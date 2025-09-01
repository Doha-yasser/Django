from django.urls import path
from .views import *



urlpatterns = [
    path('' , Home , name='myuser-home'),
    path('login/' , Login , name='myuser-login'),
    path('logout/', Logout , name='myuser-logout'),
    path('register/' ,Register , name='myuser-register'),
]

