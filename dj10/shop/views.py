from django.shortcuts import render
from . models import surendera_store

# Create your views here.

def shop1(request):
    store = surendera_store.objects.all()
    return render(request , 'shop1.html',{"store" : store} )
    