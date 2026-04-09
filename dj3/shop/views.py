from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def shop1(request,id) : 
    return HttpResponse(f" <h2> your shop id is {id} </h2>")

def shop1_name(request,name) : 
    return HttpResponse(f" <h2> your name is {name} </h2> ")

def allshops(request , **kwargs) : 
    return HttpResponse("<h3>all shopes near me {kwargs} </h3> ")
    

