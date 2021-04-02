from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import squirrel


# Create your views here.
def home(request):
    return render(request,'tracker/home.html')


def all_sightings(request):
    squirrels = squirrels.objects.all()
    context = {
            'squirrels':squirrels
            }
    return render(request,'tracker/all.html',context)



