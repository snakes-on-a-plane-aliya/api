from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField()

    def __str__(self):
        return self.name

class Passenger(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Seat(models.Model):
    name = models.CharField(max_length=256)
    flight = models.ForeignKey(Flight, on_delete=models.SET_DEFAULT)
    passenger = models.OneToOneField(
        Passenger,
        on_delete = models.SET_DEFAULT,
        primary_key = True,
    )
    def __str__(self):
        return f'The seat is {self.name}, the flight is {self.flight}, the passenger is {self.passenger}'
