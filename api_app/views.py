from django.shortcuts import render
from rest_framework import generics
from flightseats.models import Flight, Seat, Passenger
from .serializers import FlightSerializer, SeatSerializer, PassengerSerializer

class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class SeatDetail(generics.RetrieveUpdateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class PassengerList(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer