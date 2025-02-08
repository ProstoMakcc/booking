from django.urls import path
from .views import room_list, room_details

urlpatterns = [
    path("", room_list, name="room_list"),
    path("<int:pk>/", room_details, name="room_details"),
]
