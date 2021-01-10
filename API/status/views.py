from .models import Status   # Main Model
from .serializers import StatusSerializer  # Serializer Based on Status Model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView ,
    RetrieveAPIView,
    UpdateAPIView,
    )



# Create your views here.

#General APIView
class StatusAPIView(APIView):
    def get(self,request,format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list,many=True)
        return Response(status_serializer.data)
    

# if Inherite ListAPIView class , no need to define get() func under customized class. 
# know more about APIView and ListAPIView  and all Generic view, See documentation "API GUIDE ---> Generic views"

# Here StatusAPIView and StatusListAPIView provide same functionallity

class StatusListAPIView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    
    
   
class StatusCreateAPIView(CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    
    
    
class StatusDetailAPIView(RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
       
"""
# we can use looup_field instead of this code
    def get_object(self):
        kwargs = self.kwargs
        kw_id = kwargs.get('id')
        return Status.objects.get(id=kw_id)

"""


class StatusUpdateAPIView(UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
  
    
