from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import squirrel
from .forms import Form

# Create your views here.
def home(request):
    return render(request,'tracker/home.html')


def all_sightings(request):
    squirrels = squirrels.objects.all()
    context = {
            'squirrels':squirrels
            }
    return render(request,'tracker/all.html',context)

def add(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tracker/')
    else:
        form = Form()
        context = {'form':form,}
        return render(request,'tracker/form.html',context)
