from .models import Status   # Main Model
from .serializers import StatusSerializer  # Serializer Based on Status Model
from rest_framework.parsers import FormParser,MultiPartParser
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
    parser_classes = [FormParser,MultiPartParser]

    
    
    
# By using StatusDetailUpdateDeleteView class we can  retrive , update and Detele data   
    
class StatusDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    parser_classes = [FormParser,MultiPartParser]
    
    
