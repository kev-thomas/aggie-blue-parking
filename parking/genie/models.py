from django.db import models



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



class ParkingSpot(models.Model):

    owner = models.ManyToManyField(User, related_name='currentOwner')
    renter = models.ManyToManyField(User, related_name='currentRenter')
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


