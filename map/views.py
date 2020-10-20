from django.shortcuts import render
from django.shortcuts import get_object_or_404

from sightings.models import Squirrel

def index(request):

	points= Squirrel.objects.all()[:100]

	context = {
		'points': points,
	}
	return render(request, 'map/index.html', context)