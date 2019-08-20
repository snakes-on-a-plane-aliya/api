from django.contrib import admin
from .models import Flight, Passenger, Seat

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Seat)
