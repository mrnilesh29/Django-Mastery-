from django.urls import path 
from . import views

urlpatterns = [
    path('exam1' ,views.exam1, name="Exam1" )
]
