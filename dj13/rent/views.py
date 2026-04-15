from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import rent_details



# Create your views here.

def bikerent(request): 
    return render(request , "bikerent.html")

def carrent(request) : 
    return render(request , "carrent.html")


def submit(request): 
    if request.method == 'POST': 
        name = request.POST.get("username")
        age = request.POST.get("age")
        purpose = request.POST.get("purpose")
        
        if name and age:
            request.session['username'] = name 
            
            rent_details.objects.create(
                name=name,
                age=age,
                purpose=purpose
            ) 
            
            return redirect('success')
        
        else: 
            return HttpResponse("Please provide all details")

    return render(request, 'rentdetails.html')   # ✅ redirect hata diya


def success(request): 
    if 'username' in request.session: 
        return render(request, "success.html")
    
    return redirect('rent_details')
