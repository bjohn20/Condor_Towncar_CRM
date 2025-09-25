from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    # Booking URLs
    path('booking/detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('delete/detail/<int:pk>/', views.booking_delete, name='delete'),
    path('booking_add/', views.booking_add, name='add'),
    path('update/detail/<int:pk>/', views.booking_update, name='update'),
    
    # Client URLs
    path('clients/', views.client_list, name='clients'),
    path('client/add/', views.client_add, name='client_add'),
    path('client/detail/<int:pk>/', views.client_detail, name='client_detail'),
    path('client/delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('client/update/<int:pk>/', views.client_update, name='client_update'),
]