from django import forms
from .models import Booking, Client, Driver

# Create Client Form
class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ['name', 'email', 'phone_number', 'home_street', 'home_city', 'home_state', 'home_zipcode', 'client_notes']
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
      
      # Address fields
      'home_street': forms.TextInput(attrs={'class': 'form-control'}),
      'home_city': forms.TextInput(attrs={'class': 'form-control'}),
      'home_state': forms.TextInput(attrs={'class': 'form-control'}),
      'home_zipcode': forms.TextInput(attrs={'class': 'form-control'}),
      'client_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    }
    

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
  
  airport_code = forms.ChoiceField(choices=Booking.AIRPORT_CHOICES, label="Airport Code", required=False, widget=forms.Select(attrs={'class': 'form-select'}))
  
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    # If instance exists (editing), set initial values for client and driver
    if self.instance and self.instance.pk:
      self.fields['client'].initial = self.instance.client
      self.fields['driver'].initial = self.instance.driver
      
    for field_name, field in self.fields.items():
      
      if isinstance(field.widget, forms.Select) or isinstance(field.widget, forms.TimeInput):
        
        if 'form-select' not in field.widget.attrs.get('class', ''):
          field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-select'
      else:
        if 'form-control' not in field.widget.attrs.get('class', ''):
          field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'
  
  class Meta:
    model = Booking
    
    # Specify the fields to include in the form
    fields = '__all__'
    
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
    
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      # Make the fields that are sometimes optional not required in the form
      self.fields['airport_code'].required = False
    
    # --- The crucial validation logic ---
    def clean(self):
        cleaned_data = super().clean()
        service_type = cleaned_data.get("service_type")
        airport_code = cleaned_data.get("airport_code")
        
        # Enforce logic based on service type
        if service_type == 'AP':
          # Airport Pickup logic
          if not cleaned_data.get('airport_code'):
            self.add_error('airport_code', "You must select an airport for an Airport Pickup.")
            
        elif service_type == 'AD':
          # Airport Dropoff logic
          if not cleaned_data.get('pickup_street'):
            self.add_error('pickup_street', 'Street address is required for Airport Dropoff pickup.')

        return cleaned_data