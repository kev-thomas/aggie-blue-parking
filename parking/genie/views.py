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
from datetime import datetime, timedelta


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

# gets the users rentals if the token is valid
def getUserRentals(request):

    if request.method == 'GET':

        header = request.headers
        token = header['Authorization']
        bToken = token.encode('utf-8')

        try:
            payload = jwt.decode(bToken, "secret", algorithms=["HS256"])

            username = payload['username']
            permissions = payload['permissions']
            exp = payload['exp']

            print(username)
            print(permissions)

            parkingSpots = ParkingSpot.objects.filter(renter__username=username).order_by('-distance')
            parking_list = serializers.serialize('json', parkingSpots)
            dict_parking = json.loads(parking_list)[0]
            print(dict_parking)
            dict_parking['fields']['token'] = token
            json_parking = json.dumps(dict_parking['fields'])


            return HttpResponse(json_parking, content_type="text/json-comment-filtered")

        except Exception as e:



            # maybe log the exception
            print(e)

            return HttpResponse('Unauthorized', status=401)


@csrf_exempt
def login(request):

    if request.method == 'POST':

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

            exp = datetime.now() + timedelta(hours=1)
            responce_token = jwt.encode({'username': username, 'permissions': level, 'exp': exp }, 'secret', algorithm='HS256')
            content = {'token':responce_token}

            json_response = json.dumps(content)
            return HttpResponse(json_response, content_type="text/json-comment-filtered", status=200)

        else:
            return HttpResponse('Unauthorized', status=401)

            
 


# Helper Functions, not handlers =================================================================================HELPERS===================================

# authenticates the user
def auth(uname, password):

    try:
        user = User.objects.get(username=uname)
    
    except Exception as e:

        return False

    if user is None:
        return False
    else:
        if user.get_password() == password:
            return True
        else:
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

