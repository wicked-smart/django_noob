from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Airport, Flight, Passenger
# Create your views here.

def index(request):
    flights = Flight.objects.all()

    return render(request, "bookings/index.html",
    {
        "flights": flights
    }
    )


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
        passengers = flight.passengers.all()
        non_passengers = Passenger.objects.exclude(flight=flight)
    
    except Flight.DoesNotExist:
    
        return render(request, "bookings/flight.html",{
            "message": "Flight Does Not Exists! "
        }) 
    


    return render(request  ,"bookings/flight.html", 
        {
            "flight": flight,
            "passengers": passengers,
            "non_passengers": non_passengers
        }
    )

def book(request, flight_id):

    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)

    
    except KeyError:
        return render(request, "bookings/error.html", {
            "message" : "no passenger found"
        })
    
    except Flight.DoesNotExist: 
        return render(request, "bookings/error.html", {"message": "Flight Does not exists"})
    
    except Passenger.DoesNotExist: 
        return render(request, "bookings/error.html", {"message": "Passenger Does not exists"})
    
    #book the flight for passenger
    flight.passengers.add(passenger)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))



