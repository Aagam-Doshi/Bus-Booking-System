from django.db import models

class Bus(models.Model):
    busId=models.CharField(max_length=10,primary_key=True)
    startDest=models.CharField(max_length=100)
    endDest=models.CharField(max_length=100)
    maxCap=models.IntegerField()



class Customer(models.Model):
    name=models.TextField()
    id=models.TextField(primary_key=True)



class Schedule(models.Model):
    depTime=models.DateTimeField()
    arrTime=models.DateTimeField()
    busId=models.ForeignKey(Bus,on_delete=models.CASCADE)


# class Booking(models.Model):

# # Create your models here.
