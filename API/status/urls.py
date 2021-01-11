from django.urls import path
from .views import StatusListCreateView, StatusDetailAPIView



# status/ -> List , Create => GET , POST
# status/<id>/ -> Details, Delete, Update => GET ,DELETE, PUT/PATCH


urlpatterns = [
    path('status/',StatusListCreateView.as_view()),
    path('status/<id>/',StatusDetailAPIView.as_view()),

]
