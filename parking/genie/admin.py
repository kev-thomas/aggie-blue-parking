from django.contrib import admin

from .models import ParkingSpot
from .models import User

admin.site.register(ParkingSpot)
admin.site.register(User)
