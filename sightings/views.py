from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SquirrelForm
from django.db import connection
from .models import Squirrel

def all_sightings(request):
    sightings = Squirrel.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'sightings/all_sightings.html', context)

def update(request, squirrel_id):
    sighting = Squirrel.objects.filter(squirrel_id=squirrel_id).first()
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm(instance=sighting)
    return render(request,'sightings/add.html',{'form':form})

def add(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    else:
        form = SquirrelForm()

    return render(request,'sightings/add.html',{'form':form})

# Create your views here.
