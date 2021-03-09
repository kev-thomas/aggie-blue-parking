from django.contrib import admin

from .models import Owner
from .models import ParkingSpot
from .models import User

admin.site.register(Owner)
admin.site.register(ParkingSpot)
admin.site.register(User)