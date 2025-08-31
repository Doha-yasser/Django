from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Trainee
from .forms import TraineeForm
from track.models import Track


def all_trainees(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/all_trainees.html', context={'trainees': trainees})

def trainee_detail(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/trainee_detail.html', context={'trainee': trainee})

def create_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trainees')
    else:
        form = TraineeForm()
    
    return render(request, 'trainee/create_trainee.html', context={'form': form})

def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_detail', id=trainee.id)
    else:
        form = TraineeForm(instance=trainee)
    
    return render(request, 'trainee/update_trainee.html', context={'form': form, 'trainee': trainee})

def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        trainee.delete()
        return redirect('all_trainees')
    
    return render(request, 'trainee/delete_trainee.html', context={'trainee': trainee})
