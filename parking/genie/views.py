from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from .models import ParkingSpot
from .models import User
from .models import Event, Rentals
import logging
import jwt
from django.middleware import csrf
from django.contrib.auth import authenticate
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404

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

            parkingSpots = Rentals.objects.filter(renter__username__exact=username).order_by('date')
            print(parkingSpots)
            parking_list = serializers.serialize('json', parkingSpots)
            print(parking_list)
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

#get all available spots in an event
def eventDetail(request, event_id):

    if request.method == 'GET':

        event = get_object_or_404(Event, pk=event_id)

        try:
            header = request.headers
            token = header['Authorization']
            bToken = token.encode('utf-8')
            # maybe you can just get the event date from the front end, they would have it
            # need to add more auth here
            try:
                payload = jwt.decode(bToken, "secret", algorithms=["HS256"])
            except:

                response = JsonResponse({'ERROR': 'FORBIDDEN'}, status=403)
                return response

            # get all the rentals on the same day as the event
            rentals = Rentals.objects.filter(date = event.date)

            parkingSpots = ParkingSpot.objects.order_by('-distance')

            # do not add any spot that have a rental

            validSpots = []
            for spot in parkingSpots:


                valid = False
                if len(rentals) == 0:
                    valid = True

                for rental in rentals:

                    rental_spot = rental.spot.all()[0].pk
                    print(" checking ", rental_spot, " with " , spot.pk)

                    if rental_spot == spot.pk:
                        valid = False
                        break
                    else:
                        valid = True 

                if valid:
                    
                    spotData = {}
                    spotData["address"] = spot.streetAddress
                    spotData["city"] = spot.city
                    spotData["zip"] = spot.zip
                    spotData["price"] = spot.price
                    spotData["id"] = spot.pk

                    #json_spot = serializers.serialize('json', spot)
                    #dict_spot = json.loads(json_spot)
                    validSpots.append(spotData)
            
            dict_data = {}
            details = {}

            details["title"] = event.title
            details["date"] = event.date
            details["time"] = event.time
            details["streetAddress"] = event.streetAddress
            details["city"] = event.city
            details["zip"] = event.zip
            details["id"] = event.pk

            dict_data["event_details"] = details
            dict_data['available_spots'] = validSpots
            dict_data['token'] = token

            response = JsonResponse(dict_data, status=200)

            response['Access-Control-Allow-Origin'] = 'http://localhost:8080/'

            return response


        except Exception as e:

            print(e)

            response = JsonResponse({'ERROR': 'MALFORMED REQUEST'}, status=400)
            return response


#get all rentals by user

#create a rental
@csrf_exempt
def makeRental(request):

    if request.method == 'POST':

        try:
            header = request.headers
            token = header['Authorization']
            bToken = token.encode('utf-8')

            # need to add more auth here
            try:
                payload = jwt.decode(bToken, "secret", algorithms=["HS256"])
            except:

                response = JsonResponse({'ERROR': 'FORBIDDEN'}, status=403)
                return response

            eventId = json.loads(request.body)['eventId']
            spotId = json.loads(request.body)['spotId']
            userId = json.loads(request.body)['userId']


            event = get_object_or_404(Event, pk=eventId)
            spot = get_object_or_404(ParkingSpot, pk=spotId)
            renter = get_object_or_404(User, pk=userId)

            date = event.date

            # check all rentals and make sure none have the same spot at the same event and same time 
            try:
                rentals = Rentals.objects.order_by('date')

                i = 0
                for rental in rentals:

                    spot_rental = rentals[i].spot.all()[0].pk
                    event_rental = rentals[i].event.all()[0].pk

                    print("comparing:")
                    print(str(rentals[i].date) + " and " + str(date) )
                    print(str(event_rental) + " and " + str(eventId) )
                    print(str(spot_rental) + " and " + str(spotId) )

                    if rentals[i].date == date and str(spot_rental) == str(spotId):

                        content = {'message': 'spot not availble'}
                        responce = JsonResponse(content, status=409)
                        return responce

                    i += 1

                # check money
                if(renter.money >= spot.price):

                    print("debiting $" + str(spot.price))
                    renter.money = renter.money - spot.price
                    renter.save()
                else:

                    content = {'message': 'not enough money'}
                    responce = JsonResponse(content, status=409)
                    return responce



            # if it cannot get any rentals that means it's the first 
            except Exception as e:

                print("PRINTING EXCEPTION:", e)


            newRental = Rentals(
                date = date
                )
            
            newRental.save()
            newRental.spot.set(spotId)
            newRental.renter.set(userId)
            newRental.event.set(eventId)

            response = JsonResponse({'message': 'success', 'token': token}, status=200)
            return response


        except Exception as e:

            print("EXCEPTION:", e)
            response = JsonResponse({'ERROR': 'MALFORMED REQUEST'}, status=400)
            return response



# gets all the events if the token is valid
def getAllEvents(request):
    if request.method == 'GET':

        try:

            header = request.headers
            token = header['Authorization']
            bToken = token.encode('utf-8')
 
            payload = jwt.decode(bToken, "secret", algorithms=["HS256"])

            username = payload['username']
            permissions = payload['permissions']
            exp = payload['exp']

            print(username)
            print(permissions)

            events_objects = Event.objects.order_by('date')
            events_list = serializers.serialize('json', events_objects)
            dict_events = json.loads(events_list)

            # removes info about the database
            events = []
            dict_data = {}
            # Format response data to match front-end requirements
            for event in dict_events:
                dict_data = event["fields"]
                dict_data["name"] = dict_data["title"]
                dict_data["start"] = dict_data["date"] + " " + dict_data["time"]
                end_time = str(int(dict_data["time"][0:1]) + 10) + dict_data["time"][2:]
                dict_data["end"] = dict_data["date"] + " " + (dict_data["time"])
                events.append(dict_data)
            print(events)
            response = JsonResponse(events, status=200, safe=False)

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
        try:
            username = json.loads(request.body)['username']
            password = json.loads(request.body)['password']
        except KeyError:
            response = JsonResponse({'ERROR': 'MALFORMED REQUEST'}, 400)
            return response
        content = None

        print(username, password)

        if auth(username, password):

            level = getPermission(username)

            canRent = False
            canOwn = False

            exp = datetime.now() + timedelta(hours=9)
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
            newUser.save()
            return HttpResponse('OK', status=200)

@csrf_exempt
def createParking(request):
    if request.method == 'POST':
        header = request.headers
        token = header['Authorization']
        bToken = token.encode('utf-8')

        try:
            payload = jwt.decode(bToken, "secret", algorithms=["HS256"])
            username = payload['username']

            owner = User.objects.get(username = username)
            renter = None
            streetAddress = json.loads(request.body)['streetAddress']
            city = json.loads(request.body)['city']
            zip = json.loads(request.body)['zip']
            price = json.loads(request.body)['price']
            available = True
        except KeyError:
            response = JsonResponse({'ERROR' : 'MALFORMED REQUEST'}, 400)
            return response
        content = None

        newParking = ParkingSpot(
            streetAddress = streetAddress,
            city = city,
            zip = zip,
            price = price,
            available = available
        )
        newParking.save()
        newParking.owner.add(owner)
        #newParking.renter.set(None)
        newParking.save()
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
