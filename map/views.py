from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Point
from sightings.models import Squirrel

def index(request):

	points= Squirrel.objects.all()

	context = {
		'points': points,
	}
	return render(request, 'map/index.html', context)