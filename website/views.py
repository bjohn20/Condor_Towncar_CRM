from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .mixins import RedirectAuthenticatedUserMixin
from .models import Client, Booking
from .forms import BookingForm, ClientForm

# Create your views here.

class HomeView(RedirectAuthenticatedUserMixin, TemplateView):
  # The mixin will redirect authenticated users
  # The template handles unauthenticated users
  template_name = 'home.html'

class DashboardView(LoginRequiredMixin, TemplateView):
  template_name = 'dashboard.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Fetch a few bookings to show on the dashboard
    context['upcoming_bookings'] = Booking.objects.all().order_by('pickup_time')[:5]
    # Get total counts for an at-a-glance view
    context['total_bookings'] = Booking.objects.count()
    context['total_clients'] = Client.objects.count()
    return context

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    ordering = ['pickup_time']
    paginate_by = 10
    
class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking_detail.html'
    context_object_name = 'booking'
      
class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    # Success URL: Where to redirect after deletion
    # We use reverse_lazy because the URL configuration is not loaded when the file is imported
    success_url = reverse_lazy('booking_list')
    template_name = 'booking_confirm_delete.html'

class BookingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  # Create view: provides all form creation and submission handling
  model = Booking
  form_class = BookingForm
  template_name = 'booking_add.html'
  success_url = reverse_lazy('booking_list')
  success_message = "Booking created successfully."

class BookingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Booking
  form_class = BookingForm
  template_name = 'booking_update.html'
  success_url = reverse_lazy('booking_list')
  success_message = "Booking updated successfully."
      
class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    ordering = ['name']
    paginate_by = 10

class ClientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Client
  form_class = ClientForm
  template_name = 'client_add.html'
  success_url = reverse_lazy('clients')
  success_message = "Client added successfully."

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients')
    template_name = 'client_confirm_delete.html'

class ClientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Client
  form_class = ClientForm
  template_name = 'client_update.html'
  success_url = reverse_lazy('clients')
  success_message = "Client updated successfully."