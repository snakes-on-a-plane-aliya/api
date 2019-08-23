from django.shortcuts import render
from rest_framework import generics
from flightseats.models import Flight, Seat, Passenger, Player, Cell
from .serializers import FlightSerializer, SeatSerializer, PassengerSerializer, PlayerSerializer, CellSerializer

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

class PassengerDetail(generics.RetrieveUpdateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CellList(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

class CellDetail(generics.RetrieveUpdateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer