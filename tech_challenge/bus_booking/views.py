from rest_framework import status, generics
from rest_framework.response import Response
from .models import Bus, Customer, TravelDetail, Reservation
from .serializers import (
    BusSerializer,
    CustomerSerializer,
    TravelDetailSerializer,
    ReservationSerializer,
    TravelDetailUpdateAvailableSeatsSerializer,
    BookingSerializer)


# Bus Views
class BusListView(generics.ListAPIView):
    serializer_class = BusSerializer

    def get(self, request):
        buses = Bus.objects.all()
        serializer = self.serializer_class(buses, many=True)
        return Response({'success':True, 'detail':'Search result', 'data':serializer.data}, status=status.HTTP_200_OK)

   
class BusCreateView(generics.CreateAPIView):
    serializer_class= BusSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BusRetrieveView(generics.RetrieveAPIView):
    serializer_class = BusSerializer

    def get(self, request, id):
        try:
            bus = Bus.objects.get(bus_id=id)
        except Bus.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(bus)
        return Response({'success':True, 'detail':'Search result', 'data': serializer.data}, status=status.HTTP_200_OK)


class BusUpdateView(generics.UpdateAPIView):
    serializer_class = BusSerializer

    def put(self, request, id):

        try:
            bus = Bus.objects.get(bus_id=id)
        except Bus.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(bus, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully modified', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class BusDeleteView(generics.DestroyAPIView):
    serializer_class = BusSerializer

    def delete(self, request, id):

        try:
            bus = Bus.objects.get(bus_id=id)
        except Bus.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        bus.delete()
        return Response({'success':True, 'detail':'Deleted element'}, status=status.HTTP_204_NO_CONTENT)
    

# Customer Views

class CustomerListView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    
    def get(self, request):
        customers = Customer.objects.all()
        serializer = self.serializer_class(customers, many=True)
        return Response({'success':True, 'detail':'Search result', 'data':serializer.data}, status=status.HTTP_200_OK)


class CustomerCreateView(generics.CreateAPIView):
    serializer_class= CustomerSerializer

    def create_customer(self, data):
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors  

    def post(self, request):
        data = request.data
        customer = self.create_customer(data)
        if 'customer_id' in customer :
            return Response({'success':True, 'detail':'Successfully created', 'data':customer}, status=status.HTTP_201_CREATED)
        return Response({'success':False, 'detail':'Invalid data provided', 'data': customer}, status=status.HTTP_400_BAD_REQUEST) 


class CustomerRetrieveView(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer

    def get(self, request, id):
        try:
            customer = Customer.objects.get(customer_id=id)
        except Customer.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(customer)
        return Response({'success':True, 'detail':'Search result', 'data': serializer.data}, status=status.HTTP_200_OK)


class CustomerUpdateView(generics.UpdateAPIView):
    serializer_class = CustomerSerializer

    def put(self, request, id):

        try:
            customer = Customer.objects.get(customer_id=id)
        except Customer.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(customer, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully modified', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class CustomerDeleteView(generics.DestroyAPIView):
    serializer_class = CustomerSerializer

    def delete(self, request, id):

        try:
            customer = Customer.objects.get(customer_id=id)
        except Customer.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        customer.delete()
        return Response({'success':True, 'detail':'Deleted element'}, status=status.HTTP_204_NO_CONTENT)
    

# Travel Views

class TravelDetailListView(generics.ListAPIView):
    serializer_class = TravelDetailSerializer

    def get(self, request):
        travels_detail = TravelDetail.objects.all()
        serializer = self.serializer_class(travels_detail, many=True)
        return Response({'success':True, 'detail':'Search result', 'data':serializer.data}, status=status.HTTP_200_OK)
    

class TravelDetailCreateView(generics.CreateAPIView):
    serializer_class = TravelDetailSerializer

    def create_travel_detail(self, data):
        try:
            bus = Bus.objects.get(bus_id=data['bus_id'])
        except Bus.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)

        data['available_seats'] = bus.seating_capacity

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors
    
    def post(self, request):
        data = request.data
        travel_detail = self.create_travel_detail(data)

        if 'travel_detail_id' in travel_detail :
            return Response({'success':True, 'detail':'Successfully created', 'data':travel_detail}, status=status.HTTP_201_CREATED)
        return Response({'success':False, 'detail':'Invalid data provided', 'data': travel_detail}, status=status.HTTP_400_BAD_REQUEST)


class TravelDetailRetrieveView(generics.RetrieveAPIView):
    serializer_class = TravelDetailSerializer

    def get(self, request, id):
        try:
            travel_detail = TravelDetail.objects.get(customer_id=id)
        except TravelDetail.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(travel_detail)
        return Response({'success':True, 'detail':'Search result', 'data': serializer.data}, status=status.HTTP_200_OK)
    

class TravelDetailUpdateView(generics.UpdateAPIView):
    serializer_class = TravelDetailSerializer

    def put(self, request, id):

        try:
            travel_detail = TravelDetail.objects.get(travel_detail_id=id)
        except TravelDetail.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(travel_detail, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully modified', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class TravelDetailUpdateAvailableSeatsView(generics.UpdateAPIView):
    serializer_class = TravelDetailUpdateAvailableSeatsSerializer

    def update_available_seats(self, data):
        try:
            travel_detail = TravelDetail.objects.get(travel_detail_id=data['travel_detail_id'])
        
        except TravelDetail.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        if data['available_seats'] < 0:
            return Response({'success':False, 'detail':'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)

        travel_detail.available_seats = data['available_seats']
        travel_detail.save()
        return travel_detail

    def put(self, request):

        travel_detail = self.update_available_seats(request.data)
        
        serializer = self.serializer_class(travel_detail, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully modified', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TravelDetailDeleteView(generics.DestroyAPIView):
    serializer_class = TravelDetailSerializer

    def delete(self, request, id):

        try:
            travel_detail = TravelDetail.objects.get(travel_detail_id=id)
        except TravelDetail.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        travel_detail.delete()
        return Response({'success':True, 'detail':'Deleted element'}, status=status.HTTP_204_NO_CONTENT)
    

# Reservation Views

class ReservationListView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = self.serializer_class(reservations, many=True)
        return Response({'success':True, 'detail':'Search result', 'data':serializer.data}, status=status.HTTP_200_OK)
    

class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def create_reservation(self, data):

        customer = Customer.objects.filter(name=data['name'], email = data['email']).first()

        if not customer:
            instance_customer = CustomerCreateView()
            customer = instance_customer.create_customer(data)

        travel_detail_search = TravelDetail.objects.filter(origin=data['origin'], destination=data['destination'], departure_date=data['departure_date']).first()

        data['bus_id'] = 1

        if not travel_detail_search:
            instance_travel_detail = TravelDetailCreateView()
            travel_detail_new = instance_travel_detail.create_travel_detail(data)

        travel_detail = TravelDetail.objects.get(travel_detail_new['travel_detail_id'])

        data['travel_detail_id'] = travel_detail.travel_detail_id
        data['customer_id'] = customer['customer_id']

        if travel_detail.available_seats < 1:
            return Response({'success':False, 'detail':'No available seats'}, status=status.HTTP_400_BAD_REQUEST)
        
        instance_travel_detail = TravelDetailUpdateAvailableSeatsView()
        data_seats = {'travel_detail_id':data['travel_detail_id'], 'available_seats':travel_detail.available_seats-1}
        travel_detail = instance_travel_detail.update_available_seats(data_seats)

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors
    
    def post(self, request):
        data = request.data
        reservation = self.create_reservation(data)
        if 'reservation_id' in reservation :
            return Response({'success':True, 'detail':'Successfully created', 'data':reservation}, status=status.HTTP_201_CREATED)
        return Response({'success':False, 'detail':'Invalid data provided', 'data': reservation}, status=status.HTTP_400_BAD_REQUEST)
    

class ReservationRetrieveView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer

    def get(self, request, id):
        try:
            reservation = Reservation.objects.get(customer_id=id)
        except Reservation.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(reservation)
        return Response({'success':True, 'detail':'Search result', 'data': serializer.data}, status=status.HTTP_200_OK)


class ReservationUpdateView(generics.UpdateAPIView):
    serializer_class = ReservationSerializer

    def put(self, request, id):

        try:
            reservation = Reservation.objects.get(reservation_id=id)
        except Reservation.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(reservation, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success':True, 'detail':'Successfully modified', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'success':False, 'detail':'Invalid data provided', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class ReservationDeleteView(generics.DestroyAPIView):
    serializer_class = ReservationSerializer

    def delete(self, request, id):

        try:
            reservation = Reservation.objects.get(reservation_id=id)
        except Reservation.DoesNotExist:
            return Response({'success':False, 'detail':'No item found'}, status=status.HTTP_404_NOT_FOUND)
        
        reservation.delete()
        return Response({'success':True, 'detail':'Deleted element'}, status=status.HTTP_204_NO_CONTENT)    
