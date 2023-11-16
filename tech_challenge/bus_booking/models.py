from django.db import models


class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True,)
    model = models.CharField(max_length=255)
    seating_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.model} (ID: {self.bus_id})"


class TravelDetail(models.Model):
    travel_detail_id = models.AutoField(primary_key=True)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    duration = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"Travel from {self.origin} to {self.destination} (ID: {self.travel_detail_id})"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} (ID: {self.customer_id})"


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    travel_detail_id = models.ForeignKey(TravelDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation #{self.reservation_id} - Customer: {self.customer.name}, Travel: {self.travel_detail.origin} to {self.travel_detail.destination}"

