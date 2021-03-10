from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import ParkingSpot
from .models import User
import logging
import jwt
from django.middleware import csrf
from django.contrib.auth import authenticate
import json
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def login(request):

    if request.method == 'GET':

        header = request.headers
        token = header['Authorization']
        bToken = token.encode('utf-8')
        payload = jwt.decode(bToken, "secret", algorithms=["HS256"])

        username = payload['username']
        password = payload['password']
        content = None

        if auth(username, password):

            level = getPermission(username)
            
            canRent = False
            canOwn = False

            if level >= 1:
                canRent = True
            if level >= 2:
                canOwn = True

            content = {
                'responce': 'successful',
                'user': username,
                'canRent': canRent,
                'canOwn': canOwn
            }

        else:

            content = {
                'responce': 'failed',
                'user':'none',
                'canRent':'none',
                'canOwn': 'none'
            }

            
        json_response = json.dumps(content)
 
        return HttpResponse(json_response, content_type="text/json-comment-filtered")


# Helper Functions, not handlers
def auth(uname, password):

    user = User(username=uname)

    if user is None:
        print("no user")
        return False
    else:
        print(user.get_password(), password)
        if user.get_password() == password:
            return True
        else:
            print("wrong password")
            return False

# find the user by username and check what he can do
# 1 = rent only, 2 = own only, 3 = rent and own
def getPermission(uname):

    permission = 0;

    user = User(username=uname)

    if user.can_rent():
        permission += 1
    if user.can_own():
        permission += 2

    return permission

