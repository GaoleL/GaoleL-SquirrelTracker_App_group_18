from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import squirrel
from .forms import Form

# Create your views here.

def update(request,squirrel_id):
    Object = get_object_or_404(squirrel,Unique_squirrel_id=squirrel_id)
    form = Form(request.POST or None,instance=Object)
    context = {'form':form}
    if form.is_valid():
        Object=form.save(commit=False)
        Object.save()
        return redirect('/tracker/')
    else:
        context={
                'form':form,
        }
        return render(request,'tracker/detail.html',context)

def home(request):
    return render(request,'tracker/home.html')


def all_sightings(request):
    squirrels = squirrel.objects.all()
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

def all_stats(request):
    num_of_sightings = squirrel.objects.all().count()
    context = {
            'num_of_sightings':num_of_sightings,
            }
    return render(request, 'tracker/stats.html', context)
