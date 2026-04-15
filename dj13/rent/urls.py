from django.urls import path
from . import views

urlpatterns = [
    path('bikerent/', views.bikerent, name="bikerent"),
    path('carrent/', views.carrent, name="carrent"),
    path('rentdetails/', views.rent_details, name="rent_details"),
    path('submit/', views.submit, name="submit"), 
    path('success/', views.success, name="success"),
]