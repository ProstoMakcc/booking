from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, "booking/room_list.html", context=context)

def room_details(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        "room": room,
    }

    return render(request, "booking/room_details.html", context)
