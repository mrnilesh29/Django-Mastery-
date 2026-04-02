from django.shortcuts import render
from django.http import HttpResponse , request

# Create your views here.

def team1(request) : 
    return HttpResponse("this is team 1")

def team2(request) : 
    return HttpResponse("this is the team2 funtion")