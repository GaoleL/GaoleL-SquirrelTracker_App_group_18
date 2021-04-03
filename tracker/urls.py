from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
		path('',views.home),
        path('sightings/',views.all_sightings),
        path('sightings/add/',views.add,name='add'),

        
        ]
