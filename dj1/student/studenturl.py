from . import views 
from django.urls import path

urlpatterns = [
    path('student1/' , views.student1 ,name="student1")
]