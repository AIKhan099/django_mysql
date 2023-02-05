from django.db import models

# Create your models here.

class Airport(models.Model):
    city_code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"  {self.city}({self.city_code}) "

class Flights(models.Model):
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Departure')
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='Destination')
    duration=models.IntegerField()

    def __str__(self):
        return f"origin {self.origin} destination : {self.destination} duration {self.duration}"
class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
class Dummy_flights(models.Model):
    origin=models.CharField(max_length=64)
    Destination=models.CharField(max_length=64)
    duration=models.IntegerField()

    def __str__(self):
        return self.Dummy_flights

