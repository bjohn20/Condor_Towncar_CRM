from django.contrib import admin

# Register your models here.
from .models import Client, Driver, Booking

admin.site.register(Client)
admin.site.register(Driver) 
admin.site.register(Booking)