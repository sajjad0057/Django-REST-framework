from django.urls import path
from .views import StatusAPIView,StatusListAPIView,StatusCreateAPIView,StatusDetailAPIView



urlpatterns = [
    path('status/',StatusAPIView.as_view()),
    path('status/list/',StatusListAPIView.as_view()),
    path('status/create/',StatusCreateAPIView.as_view()),
    path('status/detail/<id>/',StatusDetailAPIView.as_view()),
]
