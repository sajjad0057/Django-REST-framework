from .models import Status   # Main Model
from .serializers import StatusSerializer  # Serializer Based on Status Model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView ,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    
    )



# Create your views here.

# mixins :

# By using  StatusListCreateView class we can retrive and create data 

class StatusListCreateView(CreateModelMixin,ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
    
# By using StatusDetailAPIView class we can  retrive , update and Detele data   
    
class StatusDetailAPIView(UpdateModelMixin,DestroyModelMixin,RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
    
