from django.urls import path
from .views import *



urlpatterns = [
    path('' ,Home ),
    path('login/' , Login),
    path('logout/', Logout),
    path('register/' ,Register),
]