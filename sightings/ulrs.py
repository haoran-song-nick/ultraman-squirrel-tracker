from django.urls import path

from . import views

urlpatterns = [
        path('',views.all_sightings),
        path('<int:squirrel_id>/',views.update,name='update'), 
        path('add/',views.add,name='add'),
        
]