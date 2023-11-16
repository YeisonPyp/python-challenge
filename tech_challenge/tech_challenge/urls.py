"""tech_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bus_booking import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # BUS
    path('bus/create/', views.BusCreateView.as_view(),name='bus-create'),
    path('bus-list/get/', views.BusListView.as_view(),name='get-bus'),
    path('bus-id/get/<str:id>/', views.BusRetrieveView.as_view(),name='bus-id-bus'),
    path('bus/update/<str:id>/', views.BusUpdateView.as_view(),name='bus-update'),
    path('bus/delete/<str:id>/', views.BusDeleteView.as_view(),name='bus-delete'),
    
    # CUSTOMER
    path('customer/create/', views.CustomerCreateView.as_view(),name='customer-create'),
    path('customer-list/get/', views.CustomerListView.as_view(),name='get-customer'),
    path('customer-id/get/<str:id>/', views.CustomerRetrieveView.as_view(),name='customer-id-customer'),
    path('customer/update/<str:id>/', views.CustomerUpdateView.as_view(),name='customer-update'),
    path('customer/delete/<str:id>/', views.CustomerDeleteView.as_view(),name='customer-delete'),

    # TRAVEL
    path('travel-detail/create/', views.TravelDetailCreateView.as_view(),name='travel-create'),
    path('travel-detail-list/get/', views.TravelDetailListView.as_view(),name='get-travel'),
    path('travel-detail-id/get/<str:id>/', views.TravelDetailRetrieveView.as_view(),name='travel-id-travel'),
    path('travel-detail/update/<str:id>/', views.TravelDetailUpdateView.as_view(),name='travel-update'),
    path('travel-detail/update-available-seats/', views.TravelDetailUpdateAvailableSeatsView.as_view(),name='travel-update-available-seats'),
    path('travel-detail/delete/<str:id>/', views.TravelDetailDeleteView.as_view(),name='travel-delete'),
    
    # RESERVATION
    path('reservation/create/', views.ReservationCreateView.as_view(),name='reservation-create'),
    path('reservation-list/get/', views.ReservationListView.as_view(),name='get-reservation'),
    path('reservation-id/get/<str:id>/', views.ReservationRetrieveView.as_view(),name='reservation-id-reservation'),
    path('reservation/update/<str:id>/', views.ReservationUpdateView.as_view(),name='reservation-update'),
    path('reservation/delete/<str:id>/', views.ReservationDeleteView.as_view(),name='reservation-delete'),
    

]
