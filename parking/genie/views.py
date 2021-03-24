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
    if (type(request) is None):
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
            dict_parking = json.loads(parking_list)
            print(dict_parking)

            # removes info about the database
            spots = []
            dict_data = {}
            for spot in dict_parking:
                spots.append(spot['fields'])

            dict_data['spots'] = spots
            dict_data['token'] = token

            response = JsonResponse(dict_data, status=200)

            response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

            return response

        except Exception as e:

            # maybe log the exception
            print(e)

            content = {'response': 'Unauthorized'}
            response = JsonResponse(content, status=401)

            response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

            return response


@csrf_exempt
def login(request):
    if request.method == 'POST':

        header = request.headers
        # token = header['Authorization']
        # bToken = token.encode('utf-8')
        # payload = jwt.decode(bToken, "secret", algorithms=["HS256"])
        try:
            username = json.loads(request.body)['username']
            password = json.loads(request.body)['password']
        except KeyError:
            response = JsonResponse({'ERROR': 'MALFORMED REQUEST'}, 400)
            return response
        content = None

        if auth(username, password):

            level = getPermission(username)

            canRent = False
            canOwn = False

            exp = datetime.now() + timedelta(hours=1)
            responce_token = jwt.encode({'username': username, 'permissions': level, 'exp': exp}, 'secret',
                                        algorithm='HS256')
            content = {'token': responce_token}

            response = JsonResponse(content, status=200)

            response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

            return response

        else:

            content = {'response': 'Unauthorized'}
            response = JsonResponse(content, status=401)

            response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

            return response

@csrf_exempt
def register(request):

    if request.method == 'POST':

        header = request.headers
        #token = header['Authorization']
        #bToken = token.encode('utf-8')
        #payload = jwt.decode(bToken, "secret", algorithms=["HS256"])

        print(request.body)

        try:        
            firstname = json.loads(request.body)['firstname']
            lastname = json.loads(request.body)['lastname']
            username = json.loads(request.body)['username']
            email = json.loads(request.body)['email']
            password = json.loads(request.body)['password']
            renter = json.loads(request.body)['renter']
            owner = json.loads(request.body)['owner']

        except KeyError:
            response = JsonResponse({'ERROR': 'MALFORMED REQUEST'}, 400)
            return response
        content = None

        if User.objects.filter(username=username).exists():
            return HttpResponse('Conflict', status=409)
        else:
            newUser = User(
                firstname = firstname,
                lastname = lastname,
                username = username,
                email = email,
                password = password,
                renter = renter,
                owner = owner
            )
            return HttpResponse('OK', status=200)


# Helper Functions, not handlers =================================================================================HELPERS===================================

# authenticates the user
def auth(uname, password):
    try:
        user = User.objects.get(username=uname)

    except Exception as e:
        print(e)
        return False

    if user is None:
        print('no user found')
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
