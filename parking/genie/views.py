from django.shortcuts import render
from django.http import HttpResponse

from .models import ParkingSpot

# Create your views here.

def index(request):

    parkingSpots = ParkingSpot.objects.filter(available=True).order_by('-distance')
    context = {'parkingSpots': parkingSpots}
    return render(request, 'genie/index.html', context)
