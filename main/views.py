from django.shortcuts import render

from main.models import Area


def home(request):
    return render(request, 'index.html')



def map(request):
    context = {
        'points': [Area(lat=-36.8617074, long=174.3050262, crime_rate=40) for _ in range(3)]
    }
    return render(request, 'map.html', context=context)