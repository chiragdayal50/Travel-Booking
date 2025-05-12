# from pyexpat.errors import messages
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.timezone import now
from django.contrib.auth.models import User

def travel_options(request):
    options = TravelOption.objects.all()
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')
    date = request.GET.get('date', '')

    if source:
        options = options.filter(source__icontains=source)
    if destination:
        options = options.filter(destination__icontains=destination)
    if date:
        options = options.filter(date_time__date=date)

    return render(request, 'bookings/travel_options.html', {'options': options})

@login_required
def book_ticket(request, travel_id):
    travel_option = get_object_or_404(TravelOption, travel_id=travel_id)
    
    if request.method == 'POST':
        num_seats = int(request.POST['num_seats'])
        if num_seats > travel_option.available_seats:
            return render(request, 'bookings/booking_form.html', {'error': 'Not enough seats available'})

        total_price = num_seats * travel_option.price
        # Booking.objects.create(user=request.user, travel_option=travel_option, num_seats=num_seats, total_price=total_price)
        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel_option,
            num_seats=num_seats,
            total_price=total_price,
            status='Confirmed',
            booking_date=now()
        )
        travel_option.available_seats -= num_seats
        travel_option.save()

        return redirect('my_bookings')

    return render(request, 'bookings/booking_form.html', {'travel_option': travel_option})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id, user=request.user)
    if booking.status == "Confirmed":
        booking.status = 'Cancelled'
        booking.save()
    
    booking.travel_option.available_seats += booking.num_seats
    booking.travel_option.save()

    return redirect('my_bookings')

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('travel_options')
#     else:
#         form = UserCreationForm()

#     return render(request, 'bookings/register.html', {'form': form})
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match") # type: ignore
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists") # type: ignore
            return redirect("register")

        User = User.objects.create_user(username=username, email=email, password=password1)
        User.save()
        messages.success(request, "Account created successfully! Please login.") # type: ignore
        
        return redirect("login")  # ✅ Redirect to login after successful registration

    return render(request, "bookings/register.html")



# User Login
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("travel_options")  # ✅ Redirect to home after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "bookings/login.html")


# User Logout
def logout_user(request):
    logout(request)
    return redirect('login')
