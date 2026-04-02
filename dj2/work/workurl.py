from django.urls import path 
from work import views 


urlpatterns = [ 
               path("work1" , views.work1, name="work 1"), 
               path("work2" , views.work2 , name= "work 2") 
               ]