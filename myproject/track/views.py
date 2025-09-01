from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Track
from .forms import TrackForm

# Create your views here.
def tracks(request):
    tracks = Track.objects.all()
    return render(request, 'track/tracks.html', context={'tracks': tracks})

def update(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()
            return redirect('track_detail', id=track.id)
    else:
        form = TrackForm(instance=track)
    
    return render(request, 'track/update_track.html', context={'form': form, 'track': track})

def delete(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        track.delete()
        return redirect('tracks')
    
    return render(request, 'track/delete_track.html', context={'track': track})

def getTrackById(request, id):
    track = get_object_or_404(Track, id=id)
    return render(request, 'track/show_track.html', context={'track': track})

def create_track(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracks')
    else:
        form = TrackForm()
    
    return render(request, 'track/create_track.html', context={'form': form})