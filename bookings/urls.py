from django.urls import path
from .views import travel_options, book_ticket, my_bookings, cancel_booking, register, login_user, logout_user # type: ignore

urlpatterns = [
    path('', travel_options, name='travel_options'),
    path('book/<int:travel_id>/', book_ticket, name='book_ticket'),
    path('my-bookings/', my_bookings, name='my_bookings'),
    path('cancel/<int:booking_id>/', cancel_booking, name='cancel_booking'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
