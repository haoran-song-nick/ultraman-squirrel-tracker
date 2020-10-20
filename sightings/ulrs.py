from django.urls import path

from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('sightings/',views.all_sightings, name='all_sightings'), 
        path('sightings/add/',views.add,name='add'),
        path('sightings/stats/',views.stats,name='stats'),
        path('sightings/<squirrel_id>/',views.update,name='update'),
]