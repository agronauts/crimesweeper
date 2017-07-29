import pandas as pd

from django.shortcuts import render

from main.models import Area


def home(request):
    return render(request, 'index.html')


def extract_area_data():
    crime_types = {
        'Abduction and Kidnapping',
        'Assault',
        'Blackmail and Extortion',
        'Illegal Use of Property (Except Motor Vehicles)',
        'Motor Vehicle Theft and Related Offences',
        'Robbery',
        'Sexual Assault',
        'Theft (Except Motor Vehicles)'
    }
    crime_d = pd.read_csv(open('./crime_data.csv'), quotechar='"', skipinitialspace=True, header=1)
    d2 = crime_d.groupby(['Police Area', 'ANZSOC Subdivision'])
    for crime_item in d2.Victimisations.count().items():
        print(crime_item)
    return [Area(lat=-36.8617074, long=174.3050262, crime_rate=40) for _ in range(3)]


def map(request):

    areas = extract_area_data()
    context = {
        'points': areas
    }
    return render(request, 'map.html', context=context)