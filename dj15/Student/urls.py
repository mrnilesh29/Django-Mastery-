from django.urls import path
from . import views


urlpatterns = [
    path('student1' , views.student1 , name="student"), 
    path('studentlist' , views.student_list , name="studentlist"),
    
]

