from django.urls import path
from . import views



urlpatterns = [
    path('student_add/' , views.student_add , name="student_add" ) , 
    path('studentlist/' , views.student_list , name='studentlist'),
    path('studentdetails/<int:id>' , views.student_details , name="student_details"),
    path('update/<int:id>',views.student_edit , name = "update"),
    path('delete/<int:id>' , views.student_delete , name= "delete")
    
]
