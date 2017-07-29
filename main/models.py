from django.db import models

class Area(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    crime_rate = models.IntegerField()


