from django.contrib import admin

from .models import ParkingSpot, User, Event, Rentals

admin.site.register(ParkingSpot)
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Rentals)
