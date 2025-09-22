from django.db import models

class Client (models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  
  def __str__(self):
    return super().__str__()
  
class Driver (models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=20, blank=True)
  license_number = models.CharField(max_length=50, unique=True)
  
  def __str__(self):
    return super().__str__()
  
class Booking (models.Model):
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
  pickup_location = models.CharField(max_length=255)
  dropoff_location = models.CharField(max_length=255)
  pickup_time = models.DateTimeField()
  dropoff_time = models.DateTimeField(null=True, blank=True)
  status = models.CharField(max_length=50, choices=[
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled')
  ], default='pending')
  
  def __str__(self):
    return super().__str__()
  
class Service (models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    return super().__str__()