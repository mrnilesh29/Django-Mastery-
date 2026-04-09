from django.urls import path
from . import views

urlpatterns = [
    path('testpaper1' ,views.testpaper1,name="testpaper" )
]
