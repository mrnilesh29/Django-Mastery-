from django.shortcuts import render

# Create your views here.

def bikerent(request) : 
    return render(request , 'bikerent.html')
    
