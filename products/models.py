    
from django.db import models
from users.models import User

class Producer(models.Model):
    producer = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    stock = models.FloatField()  
         
    is_verified = models.BooleanField(default=False)  # Whether the delivery is verified
    is_accepted = models.BooleanField(default=False)  # Whether the delivery request is accepted
    is_rejected = models.BooleanField(default=False)  # Whether the delivery request is rejected



