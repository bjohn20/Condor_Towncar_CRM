from django.db import models
from django.utils import timezone

class Client (models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  
  home_street = models.CharField(max_length=255, blank=True)
  home_city = models.CharField(max_length=100, blank=True)
  home_state = models.CharField(max_length=50, blank=True)
  home_zipcode = models.CharField(max_length=10, blank=True)
  client_notes = models.TextField(blank=True)
  
  def __str__(self):
    return f'{self.name}'
  
class Driver (models.Model):
  name = models.CharField(max_length=100)
  phone_number = models.CharField(max_length=20, blank=True)
  license_number = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return f'{self.name}'
  
class Booking (models.Model):
  # Metadata fields
  created_at = models.DateTimeField(auto_now_add=True)
  edited_at = models.DateTimeField(auto_now=True)
  # Foreign Keys
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
  
  SERVICE_CHOICES = [
    ('AP', 'Airport Pickup (Airport to Destination)'),
    ('AD', 'Airport Dropoff (Destination to Airport)'),
    ('PT', 'Point to Point'),
    ('HR', 'Hourly'),
    ('OT', 'Other'),
  ]
  
  # Airport Choice dropdown
  AIRPORT_CHOICES = [
    ('JFK', 'JFK'),
    ('LGA', 'LGA'),
    ('EWR', 'EWR'),
    ('HPN', 'HPN'),
    ('SWF', 'SWF'),
    ('ISP', 'ISP'),
    ('Other', 'Other'),
  ]
  
  service_type = models.CharField(max_length=2, choices=SERVICE_CHOICES, default='PT', verbose_name='Service Type')
  
  VEHICLE_CHOICES = [
    ('TC', 'Town Car (Self)'),
    ('TD', 'Town Car (Delegated)'),
    ('SUV', 'SUV'),
  ]
  
  price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)
  
  vehicle_type = models.CharField(max_length=3, choices=VEHICLE_CHOICES, default='TC')
  
  delegated_driver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Delegated Driver Name')

 # Pickup Location fields
  pickup_street = models.CharField(max_length=255, blank=True, null=True)
  pickup_city = models.CharField(max_length=100, blank=True, null=True)
  pickup_state = models.CharField(max_length=50, blank=True, null=True)
  pickup_zipcode = models.CharField(max_length=10, blank=True, null=True)

  airport_code = models.CharField(max_length=10, choices=AIRPORT_CHOICES, blank=True, null=True, default=None)

  # Destination Location fields
  destination_street = models.CharField(max_length=255)
  destination_city = models.CharField(max_length=100)
  destination_state = models.CharField(max_length=50)
  destination_zipcode = models.CharField(max_length=10)

  # Additional Booking fields
  pickup_time = models.DateTimeField()
  dropoff_time = models.DateTimeField(null=True, blank=True)
  status = models.CharField(max_length=50, choices=[
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled')
  ], default='pending')
  
  def __str__(self):
    return f'Booking {self.id} - {self.client.name} with {self.driver.name} on {self.pickup_time.strftime("%Y-%m-%d %H:%M")}'

