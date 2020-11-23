from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    justification = models.TextField(null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    area_hectares = models.FloatField(blank=True, null=True)
    states = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    iso = models.ForeignKey(Iso, on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.name