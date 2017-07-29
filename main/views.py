from collections import namedtuple

import pandas as pd

from django.shortcuts import render


Area = namedtuple('Area', ['name', 'lat', 'long', 'crimes'])

def home(request):
    return render(request, 'index.html')


def get_coord_for_area(area):
    return -36.8617074, 174.3050262


def extract_area_data():
    crime_d = pd.read_csv(open('./crime_data.csv'), quotechar='"', skipinitialspace=True, header=1)
    areas = set(crime_d['Police Area'].values)
    coords = {get_coord_for_area(area) for area in areas }
    return [Area(name, lat, long, crimes=[]) for name, (lat, long) in zip(areas, coords)]


def map(request):

    areas = extract_area_data()
    context = {
        'points': areas
    }
    return render(request, 'map.html', context=context)