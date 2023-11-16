from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bus
from .serializers import BusSerializer

class BusListView(APIView):
    serializer_class = BusSerializer

    def get(self, request):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data)
