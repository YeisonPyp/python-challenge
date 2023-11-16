from rest_framework import status, generics
from rest_framework.response import Response
from .models import Bus, Customer
from .serializers import BusSerializer, CustomerSerializer


# Bus Views
class BusListView(generics.ListAPIView):
    serializer_class = BusSerializer

    def get(self, request):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
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

