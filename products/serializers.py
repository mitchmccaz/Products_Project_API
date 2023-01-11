from rest_framework import serialiers
from .models import Products

class CarSerializer(serialiers.ModelSerializer):
    class Meta:
        model = Productfields = ['title', 'descrition','price','inventory_quantity', 'id']