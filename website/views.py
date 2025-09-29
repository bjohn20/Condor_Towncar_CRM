from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Client, Driver, Booking
from .forms import BookingForm, ClientForm

# Create your views here.
def home(request):
  if request.user.is_authenticated:
      return redirect('dashboard')
  else:
      return render(request, 'home.html', {})

@login_required
def dashboard(request):
  # Fetch a few bookings to show on the dashboard
  upcoming_bookings = Booking.objects.all().order_by('pickup_time')[:5]
  
  # Get total counts for an at-a-glance view
  total_bookings = Booking.objects.count()
  total_clients = Client.objects.count()
  
  context = {'upcoming_bookings': upcoming_bookings, 'total_bookings': total_bookings, 'total_clients': total_clients}
  
  return render(request, 'dashboard.html', context)

@login_required
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

@login_required
def booking_detail(request, pk):
    # Look up the booking
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'booking_detail.html', {'booking': booking})
  
@login_required
def booking_delete(request, pk):
    # Look up the booking
    booking = get_object_or_404(Booking, pk=pk)
    # Delete the booking
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    return redirect('booking_list')

@login_required
def booking_add(request):
  # Create the form
  if request.method == "POST":
    # Bind data from request.POST
    form = BookingForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Booking added successfully.')
      return redirect('booking_list')
    # This is a GET request
  else:
    form = BookingForm()
    # This handles the case where the form is not valid
  return render(request, 'booking_add.html', {'form': form})

@login_required
def booking_update(request, pk):
    current_booking = get_object_or_404(Booking, pk=pk)
    form = BookingForm(request.POST or None, instance=current_booking)
    if form.is_valid():
      form.save()
      messages.success(request, 'Booking updated successfully.')
      return redirect('booking_list')
    return render(request, 'booking_update.html', {'form': form})
      
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_add(request):
  if request.method == "POST":
    form = ClientForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Client added successfully.')
      return redirect('clients')
  else:
    form = ClientForm()
  return render(request, 'client_add.html', {'form': form})

@login_required 
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'Client deleted successfully.')
    return redirect('clients')

@login_required  
def client_update(request, pk):
    current_client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=current_client)
    if form.is_valid():
      form.save()
      messages.success(request, 'Client updated successfully.')
      return redirect('clients')
    return render(request, 'client_update.html', {'form': form})