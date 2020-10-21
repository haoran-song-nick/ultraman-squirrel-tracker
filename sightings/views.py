from django.shortcuts import render,redirect
from django.template import loader
from django.db.models import Count,Q
from django.db import connection

from .forms import SquirrelForm
from .models import Squirrel

def index(request):
    return render(request, 'sightings/index.html')

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
            return redirect('/squirrels/sightings/')
    else:
        form = SquirrelForm(instance=sighting)
    return render(request,'sightings/update.html',{'form':form})

def add(request):
    if request.method=='POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/squirrels/sightings/')
    else:
        form = SquirrelForm()

    return render(request,'sightings/add.html',{'form':form})

def stats(request):
    dataset = Squirrel.objects \
        .values('shift') \
        .annotate(running_count=Count('shift', filter=Q(running=True)),
                not_running_count=Count('shift', filter=Q(running=False)),
                chasing_count=Count('shift', filter=Q(chasing=True)),
                not_chasing_count=Count('shift', filter=Q(chasing=False)),
                climbing_count=Count('shift', filter=Q(climbing=True)),
                not_climbing_count=Count('shift', filter=Q(climbing=False)),
                eating_count=Count('shift', filter=Q(eating=True)),
                not_eating_count=Count('shift', filter=Q(eating=False)),
                foraging_count=Count('shift', filter=Q(foraging=True)),
                not_foraging_count=Count('shift', filter=Q(foraging=False))) \
        .order_by('shift')
    return render(request, 'sightings/stats.html', {'dataset': dataset})
