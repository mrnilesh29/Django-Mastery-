from django.urls import path 
from . import views 


urlpatterns = [
    path("work1" , views.work1 , name="Work1")
]
