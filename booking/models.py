from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    location = models.TextField(max_length=100) 
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.number

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    creation_time = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.room.number + " " + str(self.date) + " " + str(self.start_time) + " " + str(self.end_time) 
