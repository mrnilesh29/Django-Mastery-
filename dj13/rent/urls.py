from django.urls import path
from . import views

urlpatterns = [
    path('bikerent' , views.bikerent , name="bikerent app"),
    path('carrent' , views.carrent , name="car rent")
    
]
