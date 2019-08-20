from rest_framework import serializers
from flightseats.models import Flight, Seat, Passenger

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'airborne')
        model = Flight


class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'flight')
        model = Seat

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'seat')
        model = Passenger