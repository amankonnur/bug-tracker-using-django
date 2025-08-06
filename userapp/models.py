from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userdata(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional
    city = models.CharField(max_length=100)
    door_no= models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to='images/',null=True,blank=True)
