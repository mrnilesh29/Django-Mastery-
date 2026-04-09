from django.urls import path 
from . import views


urlpatterns = [
    path('typee' , views.type , name= "type")
]
