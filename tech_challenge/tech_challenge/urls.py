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

    


]
