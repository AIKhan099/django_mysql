from django.contrib import admin
from .models import Flights, Airport, Passenger
from .models import Dummy_flights
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flights)
admin.site.register(Passenger)
admin.site.register(Dummy_flights)