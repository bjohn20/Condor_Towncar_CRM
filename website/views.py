from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client, Driver, Booking, Service
# Create your views here.
def home(request):
  bookings = Booking.objects.all()
  
  # Check to see if logging in
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    # Authenticate
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      messages.success(request, "You have been logged in!")
      return redirect('home')
    else:
      messages.error(request, "There was an error logging in. Please try again...")
      return render(request, 'home.html', {})
  else:
    return render(request, 'home.html', {'bookings': bookings})

def login_user(request):
  pass

def logout_user(request):
  logout(request)
  messages.success(request, "You have been logged out...")
  return redirect('home')

def booking_detail(request, pk):
  if request.user.is_authenticated:
    # Look up the booking
    client_booking = Booking.objects.get(id=pk)
    return render(request, 'booking.html', {'client_booking': client_booking})
  else:
    messages.error(request, "You must be logged in to view that page...")
    return redirect('home')