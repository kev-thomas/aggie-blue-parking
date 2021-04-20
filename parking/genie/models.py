from django.db import models



class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    renter = models.BooleanField(default=True)
    owner = models.BooleanField(default=False)
    money = models.IntegerField(default = 100)

    def __str__(self):
        return self.username

    def can_rent(self):
        return self.renter

    def can_own(self):
        return self.owner

    def get_password(self):
        return self.password



class ParkingSpot(models.Model):

    owner = models.ManyToManyField(User, related_name='currentOwner')
    streetAddress = models.CharField(max_length = 200, default = "none")
    city = models.CharField(max_length = 200, default = "logan")
    zip = models.CharField(max_length = 200, default="84321")
    price = models.IntegerField(default = 1)
    distance = models.IntegerField(default = 2)
    available = models.BooleanField(default = True)

    def is_available(self):
        return self.available

    def __str__(self):
        return self.streetAddress


class Event(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    time = models.TimeField()
    streetAddress = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200, default = "Logan")
    zip = models.CharField(max_length = 200, default = "84321")

    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_time(self):
        return self.time

    def get_address(self):
        return self.streetAddress

    def __str__(self):

        string = self.title + "-id-" + str(self.pk)
        return string

class Rentals(models.Model):

    date = models.DateField()
    renter = models.ManyToManyField(User, related_name='currentRenter')
    spot = models.ManyToManyField(ParkingSpot, related_name='linkedSpot')
    event = models.ManyToManyField(Event, related_name='bookedEvent')
    code = models.CharField(max_length = 200, default = "none")

    def __str__(self):

        #message = str(self.spot.all()[0]) + "-on-" + str(self.date) + "-by-" + str(self.renter.all()[0])
        message = str(self.date) + " " + str(self.pk)
        return message


