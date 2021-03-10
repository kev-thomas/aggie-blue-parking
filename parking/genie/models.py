from django.db import models

# Create your models here.

class Owner(models.Model):

    name = models.CharField(max_length=200)
    address = models.CharField(max_length = 200)
    spotsOwned = models.IntegerField(default = 1)
    def __str__(self):
        return self.name


class ParkingSpot(models.Model):

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    price = models.IntegerField(default = 1)
    distance = models.IntegerField(default = 2)
    available = models.BooleanField(default = True)

    def is_available(self):
        return self.available

    def __str__(self):
        return self.address



class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    renter = models.BooleanField(default=True)
    owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def can_rent(self):
        return self.renter

    def can_own(self):
        return self.owner

    def get_password(self):
        return self.password

