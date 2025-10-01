from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Booking URLs
    path('booking_list/', views.BookingListView.as_view(), name='booking_list'),
    path('booking/detail/<int:pk>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('delete/detail/<int:pk>/', views.BookingDeleteView.as_view(), name='delete'),
    path('booking_add/', views.BookingCreateView.as_view(), name='add'),
    path('update/detail/<int:pk>/', views.BookingUpdateView.as_view(), name='update'),
    
    # Client URLs
    path('clients/', views.ClientListView.as_view(), name='clients'),
    path('client/add/', views.ClientCreateView.as_view(), name='client_add'),
    path('client/detail/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),
    path('client/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
]