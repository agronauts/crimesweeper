from collections import namedtuple

import pandas as pd

from django.shortcuts import render


Area = namedtuple('Area', ['name', 'lat', 'long', 'crimes'])

def home(request):
    return render(request, 'index.html')


def get_coord_for_area():
    lats = []
    lngs = []
    with open('police_areas_coords') as f:
        for line in f.readlines():
            if 'lat' in line:
                lats.append(float(line.split(':')[1][1:-2]))
            elif 'lng' in line:
                lngs.append(float(line.split(':')[1][1:-2]))
            elif 'parse error' in line:
                lats.append(0)
                lngs.append(0)
    return zip(lats, lngs)


def extract_area_data():
    crime_d = pd.read_csv(open('./crime_data.csv'), quotechar='"', skipinitialspace=True, header=1)
    areas = set(crime_d['Police Area'].values)
    coords = get_coord_for_area()

    return [Area(name, lat, long, crimes=[]) for name, (lat, long) in zip(areas, coords)]


def map(request):

    areas = extract_area_data()
    print(areas)
    context = {
        'points': areas
    }
    return render(request, 'map.html', context=context)