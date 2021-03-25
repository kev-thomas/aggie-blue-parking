from django.contrib import admin

from .models import ParkingSpot
from .models import User
from .models import Event

admin.site.register(ParkingSpot)
admin.site.register(User)
admin.site.register(Event)
