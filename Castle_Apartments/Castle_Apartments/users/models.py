from django.db import models
from django.contrib.auth.models import User
from apartments.models import Apartment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=999)
    profile_image = models.CharField(max_length=999)
    
class ViewingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)
