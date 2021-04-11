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
    AM_count = 0
    PM_count = 0
    for i in squirrel.objects.all():
        if i.Shift == 'AM':
            AM_count+=1
        if i.Shift == 'PM':
            PM_count+=1
    gray_fur_count= squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    chasing_count=squirrel.objects.filter(Chasing='True').count()
    context = {
            'AM_count':AM_count,
            'PM_count':PM_count,
            'num_of_sightings':num_of_sightings,
            'gray_fur_count':gray_fur_count,
            'chasing_count':chasing_count,
            }
    return render(request, 'tracker/stats.html', context)

def squirrel_map(request):
    sightings= squirrel.objects.all()[:100]
    context ={
            'sightings':sightings,
             }
    return render(request, 'tracker/map.html', context)
