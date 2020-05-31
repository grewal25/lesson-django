
from django.shortcuts import render
from .models import Wall

def wall_list(request):
    wall = Wall.objects.all()
    return render(request,
                  'homepage/index.html',
                  {'wall': wall})
