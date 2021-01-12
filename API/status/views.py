from .models import Status   # Main Model
from .serializers import StatusSerializer  # Serializer Based on Status Model
#if we deal with file handling , Must include parsers , otherwise no need to include parsers
from rest_framework.parsers import FormParser,MultiPartParser
# Easely build  CRUD operation API and Perform CRUD operation on Model,By using just ViewSet 
from rest_framework.viewsets import ModelViewSet




# Create your views here.

# Easely build  CRUD operation API and Perform CRUD operation on Model,By using just ViewSet   
   
class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    #if we deal with file handling , Must include parsers , otherwise no need to include parsers
     
    parser_classes = [FormParser,MultiPartParser]

    
    
    
