from django.db import models
from django.contrib.auth.models import User

class Apartment(models.Model):
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=3)
    description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    size = models.IntegerField()
    rooms = models.IntegerField()
    type = models.CharField(max_length=20)
    time_added = models.DateTimeField(auto_now_add=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.time_added)

class ApartmentImage(models.Model):
    image = models.CharField(max_length=999)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
