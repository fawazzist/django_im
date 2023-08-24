import datetime
from django.db import models
from users.models import User

class Delivery(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    quantity = models.FloatField()
    serial_number = models.CharField(max_length=100,unique=True)
    delivery_date = models.DateField()
    delivery_date = models.DateField(null=True)
    is_delivered = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


