from django.urls import path

from . import views

urlpatterns = [
        path('',views.all_sightings, name='all_sightings'),
        path('<squirrel_id>/',views.update,name='update'), 
        path('add/',views.add,name='add'),
        path('stats/',views.stats,name='stats'),
]