from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('booking/detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('delete/detail/<int:pk>/', views.booking_delete, name='booking_delete'),
    path('booking_add/', views.booking_add, name='add'),
]