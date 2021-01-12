from django.urls import path
from .views import StatusViewSet
# If use ViewSet ,when need to routers, 
# routers create automatically API end point, So we do't need to create URL 
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'status',StatusViewSet,basename = "status")

router



urlpatterns = [

] + router.urls
