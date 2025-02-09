from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Bus(models.Model):
    busId=models.CharField(max_length=10,primary_key=True)
    startDest=models.CharField(max_length=100)
    endDest=models.CharField(max_length=100)
    maxCap=models.IntegerField()



# class Customer(models.Model):
#     name=models.TextField()
#     id=models.TextField(primary_key=True)
class MyUser(AbstractUser):
    walletAmt=models.IntegerField(default=0)



class Schedule(models.Model):
    depTime=models.DateTimeField()
    arrTime=models.DateTimeField()
    busId=models.ForeignKey(Bus,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)


class Booking(models.Model):
    pasNam=models.CharField(max_length=45)
    customer=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    schedule=models.ForeignKey(Schedule,on_delete=models.SET_NULL,null=True)





# # Create your models here.
