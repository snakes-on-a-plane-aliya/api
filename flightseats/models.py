from django.db import models

class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField()

    def __str__(self):
        return self.name

class Seat(models.Model):
    name = models.CharField(max_length=256)
    flight = models.ForeignKey(Flight, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return f'The seat is {self.name}, on flight {self.flight}'


class Passenger(models.Model):
    name = models.CharField(max_length=256)
    seat = models.OneToOneField(
        Seat,
        on_delete = models.SET_DEFAULT,
        default=None,
        primary_key = True,
    )
    def __str__(self):
        return f'Passenger {self.name} has seat {self.seat}'