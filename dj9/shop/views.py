from django.shortcuts import render

# Create your views here.
def shop1(request) : 
    return render(request, "shop.html")