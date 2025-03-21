# booking

# Short info about project:

Project implements basic functionality for booking system

This project is created for learning more about django framework

# Functionality of project:

# Models

Room:
number,
capacity,
location,
price

Booking:
room,
user,
start_time,
end_time,
creation_time

ExtendedUser (extends AbstractUser model from django):
Phone number

# Url paths:
Homepage at /

Room info at /"room_number"/

Booking form at /book/

Login form at /auth/login/

Register form at /auth/register/

Logout path at /auth/logout/

# Views:
room_list - Shows homepage with list of rooms

room_details - Shows details for specific room

book_room - Renders booking form(login_required)

login_view - Renders login form

register_view - Renders register form

logout - Logouts user

# How to start project
Install django

Clone repo

Write into console: py manage.py runserver

Go to: http://127.0.0.1:8000/

Admin username: Max

Admin password: 1234
