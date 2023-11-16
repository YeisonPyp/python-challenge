from rest_framework import serializers
from .models import Bus, TravelDetail, Customer, Reservation

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class TravelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelDetail
        fields = '__all__'

class TravelDetailUpdateAvailableSeatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TravelDetail
        fields = ['available_seats']
        extra_kwargs = {'available_seats': {'required': True}}
    

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(source='customer_id', read_only=True)
    travel_detail = TravelDetailSerializer(source='travel_detail_id', read_only=True)

    class Meta:
        model = Reservation
        fields = ['reservation_id', 'customer', 'travel_detail']
