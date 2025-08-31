from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    path('', allTracks, name='all_tracks'),
    path('create/', create_track, name='create_track'),
    path('update/<int:id>/', update, name='update_track'),
    path('delete/<int:id>/', delete, name='delete_track'),
    path('<int:id>/', getTrackById, name='track_detail'),
]