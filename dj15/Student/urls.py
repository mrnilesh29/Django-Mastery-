from django.urls import path
from . import views


urlpatterns = [
    path('student1' , views.student1 , name="student"), 
    path('studentlist' , views.student_list , name="studentlist"),
    path('studentedit/<int:id>' , views.student_edit , name="Student_edit"), 
    
]

