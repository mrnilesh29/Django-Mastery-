from django.shortcuts import render

# Create your views here.

def bikerent(request): 
    return render(request , "bikerent.html")

def carrent(request) : 
    return render(request , "carrent.html")