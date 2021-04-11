from django.urls import path
from . import views
from django.conf.urls import url
from .views import all_sightings,add,all_stats

urlpatterns=[
		path('',views.home),
        path('sightings/',views.all_sightings),
        path('sightings/add/',views.add,name='add'),
        path('sightings/<squirrel_id>/', views.update,name='update'),
        path('sightings/stats',views.all_stats),
        path('map/',views.squirrel_map),
        ]
