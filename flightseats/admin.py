from django.contrib import admin
from .models import Flight, Passenger, Seat, Player, Cell

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Seat)
admin.site.register(Player)
admin.site.register(Cell)

