from django.urls import path
from .views import room_list, room_details, book_room

urlpatterns = [
    path("", room_list, name="room-list"),
    path("<int:pk>/", room_details, name="room-details"),
    path("book/", book_room, name="book-room"),
]
