
from django.shortcuts import render, get_object_or_404
from .models import Wall

def index(request):
    return render(request, 'homepage/index.html')

def wall_list(request):
    walls = Wall.objects.all()
    return render(request,
                  'homepage/list.html',
                  {'walls': walls})

def wall_detail(request, publisher_id):
    wall =  Wall.objects.get(pk=publisher_id)
    context = {'wall': wall}
    return render(request, 'homepage/detail.html', context)
