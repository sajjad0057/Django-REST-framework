from .models import Status   # Main Model
from .serializers import StatusSerializer  # Serializer Based on Status Model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    
    )



# Create your views here.

# mixins :

# By using  StatusListCreateView class we can retrive and create data 

class StatusListCreateView(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    
    
    
# By using StatusDetailAPIView class we can  retrive , update and Detele data   
    
class StatusDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    
    
