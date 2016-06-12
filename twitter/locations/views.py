from rest_framework.generics import ListAPIView

from .models import Location

from .serializers import LocationSerializer

# Create your views here.


class LocationListAPIView(ListAPIView):
    model = Location
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
