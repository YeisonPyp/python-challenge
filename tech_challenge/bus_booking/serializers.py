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

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
