from django import forms
from .models import Booking, Client, Driver

# Create Add Booking Form
class BookingForm(forms.ModelForm):
  
  # Client and Driver dropdowns
  client = forms.ModelChoiceField(queryset=Client.objects.all(), label="Client", widget=forms.Select(attrs={'class': 'form-select'}))
  
  driver = forms.ModelChoiceField(queryset=Driver.objects.all(), label="Driver", widget=forms.Select(attrs={'class': 'form-select'}))
  
  delegated_driver_name = forms.CharField(max_length=100, label="Delegated Driver Name", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
  
  # Service dropdown
  service_type = forms.ChoiceField(choices=Booking.SERVICE_CHOICES, label="Service Type", widget=forms.Select(attrs={'class': 'form-select'}))
  
  # Vehicle Type dropdown
  vehicle_type = forms.ChoiceField(choices=Booking.VEHICLE_CHOICES, label="Vehicle Type", widget=forms.Select(attrs={'class': 'form-select'}))
  
  class Meta:
    model = Booking
    
    # Specify the fields to include in the form
    fields = ('client', 'driver', 'service_type', 'price', 'vehicle_type', 'delegated_driver_name', 'pickup_street', 'pickup_city', 'pickup_state', 'pickup_zipcode', 'destination_street', 'destination_city', 'destination_state', 'destination_zipcode', 'pickup_time', 'dropoff_time', 'status')
    
    
    widgets = { 
        # Style the widgets
        'pickup_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        'dropoff_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        
        # Price and delegated driver name (no need to redefine, just widget style)
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'delegated_driver_name': forms.TextInput(attrs={'class': 'form-control'}),
        
        # All Address fields (Handled by model, just setting the widget class)
        'pickup_street': forms.TextInput(attrs={'class': 'form-control'}),
        'pickup_city': forms.TextInput(attrs={'class': 'form-control'}),
        'pickup_state': forms.TextInput(attrs={'class': 'form-control'}),
        'pickup_zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_street': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_city': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_state': forms.TextInput(attrs={'class': 'form-control'}),
        'destination_zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        
        # Status dropdown
        'status': forms.Select(attrs={'class': 'form-select'}),
    }
    
    # Labels (override default labels if needed)
    labels = {
      'price': 'Final Price ($)',
      'delegated_driver_name': 'Delegated Driver Name (if applicable)',
    }