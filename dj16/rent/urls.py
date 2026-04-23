from django.urls import path
from . import views

urlpatterns = [
    path('rent2', views.rent2, name='rent2'),
]