from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    arrival_date =  models.DateField()   
    num_of_days =  models.IntegerField()
    number_of_rooms = models.IntegerField()
    number_of_adults = models.IntegerField()
    number_of_kids = models.IntegerField()
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.first_name
    
'''class User(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    username=models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    
    def __str__(self):
        return self.last_name'''
    