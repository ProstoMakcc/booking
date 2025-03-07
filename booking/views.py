from django.shortcuts import render
from .models import Room, Booking
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def room_list(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }

    return render(request, "booking/room-list.html", context=context)

def room_details(request, pk):
    room = Room.objects.get(id=pk)
    context = {
        "room": room,
    }

    return render(request, "booking/room-details.html", context)

@login_required
def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("start-time")
        end_time = request.POST.get("end-time")

        try:
            room = Room.objects.get(number=room_number)
        except Room.DoesNotExist:
            return HttpResponse("Room not found", 404)
        
        booking = Booking.objects.create(room=room,
                                         user=request.user,
                                         start_time=start_time,
                                         end_time=end_time)
        booking.save()
        
        return HttpResponse("Room booked", 200)
    elif request.method == "GET":
        return render(request, "booking/booking-form.html")

    return HttpResponse("Method not allowed", 405)
