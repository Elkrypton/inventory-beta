#loading db.models
from django.db import models


class Manufacturer(models.Model):
    """Manufacturer model for products details"""
    item = models.CharField(max_length=50)
    quantity = models.IntegerField()
    date_of_production = models.DateTimeField()
    sku = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=50)


class Note(models.Model):
    """Note Model for feedback functionality"""
    name = models.CharField(max_length=50)
    feedback = models.TextField(max_length=600)


class SearchProduct(models.Model):
    """Seach product model for retrieve information"""
    query = models.CharField(max_length=100)
