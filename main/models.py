from django.db import models

class Area(models.Model):
    lat = models.FloatField()
    long = models.FloatField()
    crime_rate = models.IntegerField()

class CrimeType(models.Model):
    crime_type = models.CharField(max_length=60)
    crimes = models.IntegerField()


