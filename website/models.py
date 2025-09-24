from django.db import models
from django.utils import timezone

class Client (models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  
  def __str__(self):
    return f'{self.name}'
  
class Driver (models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  license_number = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return f'{self.name}'
  

class Service (models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return f'{self.name} - ${self.price}'
  
class Booking (models.Model):
  # Metadata fields
  created_at = models.DateTimeField(auto_now_add=True)
  edited_at = models.DateTimeField(auto_now=True)
  # Foreign Keys
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
  service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)

 # Pickup Location fields
  pickup_street = models.CharField(max_length=255)
  pickup_city = models.CharField(max_length=100)
  pickup_state = models.CharField(max_length=50)
  pickup_zipcode = models.CharField(max_length=10)

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
    return f'Booking {self.id} - {self.client.name} with {self.driver.name} - {self.service}'
  