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
    available = models.BooleanField(default = True)

    def is_available(self):
        return self.available

    def __str__(self):
        return self.address



