from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import ParkingSpot
import logging

from django.conf import settings

fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)
logging.debug("Logging started on %s for %s" % (logging.root.name, logging.getLevelName(lvl)))

def index(request):

    # add request handling for auth
    if(type(request) is None):
        logging.debug("no request")
    else:
        logging.debug("this is the type of the request" + str(request.body))

    parkingSpots = ParkingSpot.objects.filter(available=True).order_by('-distance')
    parking_list = serializers.serialize('json', parkingSpots)
    return HttpResponse(parking_list, content_type="text/json-comment-filtered")
