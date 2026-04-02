from django.urls import path 
from team import views

urlpatterns = [
    path("team1" ,views.team1 , name="team 1") , 
    path("team2" , views.team2 , name= "team2")
    
]