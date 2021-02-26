from django.contrib import admin

from .models import Owner
from .models import ParkingSpot

admin.site.register(Owner)
admin.site.register(ParkingSpot)
